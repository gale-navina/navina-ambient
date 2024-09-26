import numpy as np
from models.enums import RecordingStatus


class AudioBuffer:
    SAMPLE_RATE = 16000
    CHANNELS = 1
    BYTES_PER_SAMPLE = 2  # 16-bit samples
    BYTES_PER_SECOND = SAMPLE_RATE * CHANNELS * BYTES_PER_SAMPLE

    def __init__(self):
        # initial bunner as an empty 2-d array
        self.buffer = np.array([], dtype=np.int16).reshape(0, self.CHANNELS)
        self.vad_results = []
        self.last_processed_sample = 0
        self.last_transcribed_sample = 0
        self.recording_status = RecordingStatus.ACTIVE

    def append(self, new_data: np.ndarray):
        self.buffer = np.concatenate((self.buffer, new_data))

    def get_chunk(self, start: int, end: int) -> np.ndarray:
        return self.buffer[start:end]

    def get_duration(self) -> float:
        return len(self.buffer) / self.SAMPLE_RATE

    def get_total_samples(self) -> int:
        return self.buffer.shape[0]

    def get_unprocessed_samples(self) -> int:
        return self.get_total_samples() - self.last_processed_sample

    def get_untranscribed_samples(self) -> int:
        return self.get_total_samples() - self.last_transcribed_sample
