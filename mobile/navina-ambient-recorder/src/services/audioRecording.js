import {Audio} from 'expo-av';
import * as FileSystem from 'expo-file-system';
import {KinesisClient, PutRecordCommand} from "@aws-sdk/client-kinesis";

const CHUNK_DURATION = 2500; // 2.5 seconds
const LOCAL_AWS_ENDPOINT = 'http://192.168.68.103:4566';

let recording = null;
let lastSentTimestamp = 0;
let recordingDuration = 0;

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
        outputFormat: Audio.RECORDING_OPTION_ANDROID_OUTPUT_FORMAT_DEFAULT,
        audioEncoder: Audio.RECORDING_OPTION_ANDROID_AUDIO_ENCODER_DEFAULT,
        sampleRate: 16000,
        numberOfChannels: 1,
        bitRate: 256000,
    },
};

export const startRecording = async (sessionInfo, recordingId, streamConfig) => {
    try {
        await Audio.requestPermissionsAsync();
        await Audio.setAudioModeAsync({
            allowsRecordingIOS: true,
            playsInSilentModeIOS: true,
        });

        const newRecording = new Audio.Recording();
        await newRecording.prepareToRecordAsync(recordingOptions);
        newRecording.setOnRecordingStatusUpdate(status => sendAudioChunk(status, streamConfig, recordingId));
        newRecording.setProgressUpdateInterval(CHUNK_DURATION);
        await newRecording.startAsync();

        recording = newRecording;
        lastSentTimestamp = 0;
        recordingDuration = 0;

        return true;
    } catch (error) {
        console.error('Failed to start recording', error);
        return false;
    }
};

export const pauseRecording = async () => {
    if (recording) {
        await recording.pauseAsync();
    }
};

export const resumeRecording = async () => {
    if (recording) {
        await recording.startAsync();
    }
};

export const stopRecording = async () => {
    if (recording) {
        await recording.stopAndUnloadAsync();
        recording = null;
        lastSentTimestamp = 0;
        recordingDuration = 0;
    }
};

export const getRecordingStatus = async () => {
    if (recording) {
        return await recording.getStatusAsync();
    }
    return null;
};


const sendAudioChunk = async (status, streamConfig, recordingId) => {
    if (!status.isRecording || !streamConfig || !recording) {
        return;
    }

    recordingDuration = status.durationMillis;

    try {
        const uri = recording.getURI();
        const sampleRate = recordingOptions.ios.sampleRate;
        const numberOfChannels = recordingOptions.ios.numberOfChannels;
        const bitDepth = 16;
        const bytesPerSample = (bitDepth / 8) * numberOfChannels;
        const bytesPerSecond = sampleRate * bytesPerSample;

        const startPosition = Math.floor((lastSentTimestamp / 1000) * bytesPerSecond) + 44;  // Skip header

        const fileInfo = await FileSystem.getInfoAsync(uri);
        const availableBytes = fileInfo.size - startPosition;


        const chunkLength = Math.min(bytesPerSecond * CHUNK_DURATION / 1000, availableBytes);

        const chunk = await FileSystem.readAsStringAsync(uri, {
            encoding: FileSystem.EncodingType.Base64,
            length: chunkLength,
            position: startPosition,
        });

        const kinesisClient = new KinesisClient({
            endpoint: LOCAL_AWS_ENDPOINT,
            region: streamConfig.region,
            credentials: streamConfig.credentials,
            runtime: 'react-native',
        });

        const command = new PutRecordCommand({
            Data: chunk,
            StreamName: streamConfig.streamName,
            PartitionKey: recordingId,
        });

        await kinesisClient.send(command);

        const sentSeconds = chunkLength / bytesPerSecond;
        lastSentTimestamp += sentSeconds * 1000;

    } catch (error) {
        console.error('Error sending audio chunk:', error);
        // Implement retry logic here if needed
    }
};

export const getRecordingDuration = () => recordingDuration;

export const getCurrentTimestamp = () => Math.floor(Date.now() / 1000);