import {Audio} from 'expo-av';
import * as FileSystem from 'expo-file-system';
import {KinesisClient, PutRecordCommand} from "@aws-sdk/client-kinesis";

const LOCAL_AWS_ENDPOINT = 'http://192.168.68.103:4566';

const recordingOptions = {
    isMeteringEnabled: true,
    ios: {
        extension: '.wav',
        outputFormat: Audio.IOSOutputFormat.LINEARPCM,
        sampleRate: 16000,
        numberOfChannels: 1,
        bitRate: 256000,
        linearPCMBitDepth: 16,
        linearPCMIsBigEndian: false,
    },
    android: {
        extension: '.wav',
        sampleRate: 16000,
        numberOfChannels: 1,
        bitRate: 256000,
    },
};

// Calculate bytes per sample and bytes per second
const bytesPerSample = (recordingOptions.ios.linearPCMBitDepth / 8) * recordingOptions.ios.numberOfChannels;
const bytesPerSecond = recordingOptions.ios.sampleRate * bytesPerSample; // 32000 bytes per second

const CHUNK_DURATION_MS = 2500; // 2.5 seconds
const CHUNK_SIZE = Math.floor((bytesPerSecond * CHUNK_DURATION_MS) / 1000); // Ensure integer value

// Ensure CHUNK_SIZE is a multiple of 2
const CHUNK_SIZE_ADJUSTED = CHUNK_SIZE - (CHUNK_SIZE % 2);

const CHUNK_DURATION = CHUNK_DURATION_MS; // For clarity

class RecordingManager {
    constructor(streamConfig, recordingId) {
        this.recording = null;
        this.lastSentPosition = 44; // Start after the 44-byte WAV header
        this.streamConfig = streamConfig;
        this.recordingId = recordingId;
        this.isPaused = false;
        this.isSending = false;
        this.chunkTimer = null; // Add this line
    }

    async startRecording() {
        try {
            await Audio.requestPermissionsAsync();
            await Audio.setAudioModeAsync({
                allowsRecordingIOS: true,
                playsInSilentModeIOS: true,
            });

            const newRecording = new Audio.Recording();
            await newRecording.prepareToRecordAsync(recordingOptions);

            // Remove the sendAudioChunk binding from onRecordingStatusUpdate
            newRecording.setOnRecordingStatusUpdate(this.onRecordingStatusUpdate.bind(this));
            newRecording.setProgressUpdateInterval(100); // Set a smaller interval for UI updates

            await newRecording.startAsync();

            this.recording = newRecording;
            this.lastSentPosition = 44; // Initialize here
            this.isPaused = false;

            // Start the chunk sending timer
            this.startChunkTimer();

            return true;
        } catch (error) {
            console.error('Failed to start recording', error);
            return false;
        }
    }

    onRecordingStatusUpdate(status) {
        // You can update any UI-related status here
        // For example, update recording duration, metering, etc.
        // This method will be called frequently for UI updates
    }

    startChunkTimer() {
        if (this.chunkTimer) {
            clearInterval(this.chunkTimer);
        }
        this.chunkTimer = setInterval(() => {
            this.sendAudioChunk();
        }, CHUNK_DURATION);
    }

    stopChunkTimer() {
        if (this.chunkTimer) {
            clearInterval(this.chunkTimer);
            this.chunkTimer = null;
        }
    }


    async pause() {
        this.isPaused = true;
        if (this.recording) {
            await this.recording.pauseAsync(); // Pause the recording
            // Do not stop the chunk timer
        }
    }

    async resume() {
        if (this.recording) {
            await this.recording.startAsync(); // Resume the recording
            this.isPaused = false;
            // The chunk timer is already running
        }
    }

    getCurrentTimestamp() {
        return Math.floor(Date.now() / 1000);
    }

    async stopRecording() {
        if (this.recording) {
            await this.recording.stopAndUnloadAsync();
            this.recording = null;
            this.stopChunkTimer();
            await this.sendAudioChunk(); // Send any remaining data
            this.lastSentPosition = 44; // Reset to initial value
        }
    }

    async getRecordingStatus() {
        if (this.recording) {
            return await this.recording.getStatusAsync();
        }
        return null;
    }

    async sendAudioChunk() {
        if (this.isSending) {
            // Prevent overlapping calls
            console.warn('sendAudioChunk is already running');
            return;
        }

        this.isSending = true; // Acquire the lock

        try {
            if (!this.streamConfig || !this.recording) {
                return;
            }

            const uri = this.recording.getURI();

            // Get file info
            const fileInfo = await FileSystem.getInfoAsync(uri);
            const fileSize = fileInfo.size;

            const startPosition = this.lastSentPosition;
            const availableBytes = fileSize - startPosition;

            if (availableBytes <= 0) {
                return;
            }

            const chunkLength = Math.min(CHUNK_SIZE_ADJUSTED, availableBytes);

            // Ensure chunkLength is a multiple of 2
            const adjustedChunkLength = chunkLength - (chunkLength % 2);

            console.log(`Audio file size: ${fileSize} bytes`);
            console.log(`Sending chunk from position ${startPosition} with length ${adjustedChunkLength}`);

            const chunk = await FileSystem.readAsStringAsync(uri, {
                encoding: FileSystem.EncodingType.Base64,
                length: adjustedChunkLength,
                position: startPosition,
            });

            const kinesisClient = new KinesisClient({
                endpoint: LOCAL_AWS_ENDPOINT,
                region: this.streamConfig.region,
                credentials: this.streamConfig.credentials,
                runtime: 'react-native',
            });

            const command = new PutRecordCommand({
                Data: chunk,
                StreamName: this.streamConfig.streamName,
                PartitionKey: this.recordingId,
            });

            await kinesisClient.send(command);

            // Update lastSentPosition
            this.lastSentPosition += adjustedChunkLength;

        } catch (error) {
            console.error('Error sending audio chunk:', error);
            // Implement retry logic here if needed
        } finally {
            this.isSending = false; // Release the lock
        }
    }
}

export default RecordingManager;