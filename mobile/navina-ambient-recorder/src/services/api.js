import 'react-native-get-random-values';
import {KinesisClient, PutRecordCommand} from "@aws-sdk/client-kinesis";

const CORE_SERVICE_URL = 'http://172.20.4.45:8000';
const LOCAL_AWS_ENDPOINT = 'http://172.20.4.45:4566';

export const pairDevice = async (sessionId, token) => {
    const response = await fetch(`${CORE_SERVICE_URL}/pair`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({sessionId, token}),
    });

    if (!response.ok) {
        throw new Error('Failed to pair device');
    }

    return response.json();
};

export const notifyRecordingStatus = async (sessionId, recordingId, action, timestamp) => {
    await fetch(`${CORE_SERVICE_URL}/recording`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({sessionId, recordingId, action, timestamp}),
    });
};

export const sendAudioChunkToKinesis = async (chunk, streamConfig, recordingId) => {
    try {
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
    } catch (error) {
        console.error('Error sending audio chunk to Kinesis:', error);
        throw error;
    }
};