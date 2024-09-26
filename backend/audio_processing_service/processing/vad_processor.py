import numpy as np
import torch
from pyannote.audio import Model
from pyannote.audio.utils.powerset import Powerset
from scipy import signal
import logging
from config import (
    VAD_MODEL_PATH, VAD_MAX_SPEAKERS, VAD_MAX_SPEAKERS_PER_FRAME,
    SAMPLE_RATE, TARGET_FRAME_RATE, SEGMENTATION_FRAME_DURATION
)

logger = logging.getLogger(__name__)


class VADProcessor:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        self.model = Model.from_pretrained(VAD_MODEL_PATH).to(self.device)
        self.to_multilabel = Powerset(VAD_MAX_SPEAKERS, VAD_MAX_SPEAKERS_PER_FRAME).to_multilabel
        self.chunk_duration = SEGMENTATION_FRAME_DURATION

    async def process(self, audio_buffer, force_process=False):
        chunk_samples = int(SAMPLE_RATE * self.chunk_duration)
        remaining_samples = audio_buffer.get_unprocessed_samples()

        vad_results = []

        while remaining_samples > 0:
            if remaining_samples >= chunk_samples or force_process:
                chunk_start = audio_buffer.last_processed_sample
                chunk_end = chunk_start + min(remaining_samples, chunk_samples)
                audio_segment = audio_buffer.get_chunk(chunk_start, chunk_end)
                logger.info(f"Processing VAD chunk: {chunk_start}-{chunk_end}")

                vad_result = await self._run_vad_segmentation(audio_segment)
                logger.info(f"ved_result total 1 vs 0: {sum(vad_result)} vs {len(vad_result) - sum(vad_result)}")
                if vad_result is not None:
                    vad_results.extend(vad_result)
                    logger.debug(f"Processed VAD chunk: {chunk_start}-{chunk_end}, result length: {len(vad_result)}")

                audio_buffer.last_processed_sample = chunk_end
                remaining_samples = audio_buffer.get_unprocessed_samples()
            else:
                break

        audio_buffer.vad_results.extend(vad_results)
        return vad_results

    async def _run_vad_segmentation(self, audio_segment: np.array) -> np.array:
        try:
            resampled_audio = self._resample_audio(audio_segment)
            input_tensor = torch.tensor(resampled_audio, dtype=torch.float32, device=self.device).reshape(1, 1, -1)

            with torch.no_grad():
                powerset_encoding = self.model(input_tensor)

            multilabel_encoding = self.to_multilabel(powerset_encoding).cpu().numpy()
            speech_activity = multilabel_encoding.squeeze(0).sum(axis=-1)

            interpolated_labels = np.interp(
                np.arange(len(resampled_audio)),
                np.linspace(0, len(resampled_audio), len(speech_activity)),
                speech_activity
            )

            return (interpolated_labels > 0.5).astype(int)
        except Exception as e:
            logger.error(f"Error in VAD segmentation: {str(e)}")
            return None

    @staticmethod
    def _resample_audio(audio_segment: np.array) -> np.array:
        if audio_segment.shape[0] == TARGET_FRAME_RATE:
            return audio_segment

        number_of_samples = round(len(audio_segment) * float(TARGET_FRAME_RATE) / SAMPLE_RATE)
        return signal.resample(audio_segment, number_of_samples)
