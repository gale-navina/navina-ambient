import React, {useState, useEffect, useCallback, useRef} from 'react';
import {View, Text, StyleSheet, Alert, Dimensions, TouchableOpacity, Platform, ActivityIndicator} from 'react-native';
import {Audio} from 'expo-av';
import * as FileSystem from 'expo-file-system';
import QRScanner from '../components/QRScanner';
import {KinesisClient, PutRecordCommand} from "@aws-sdk/client-kinesis";
import 'react-native-get-random-values';
import 'react-native-url-polyfill/auto';
import {ReadableStream} from "web-streams-polyfill";
import {Camera, Mic, Pause, Play, Square} from 'lucide-react-native';

if (typeof global.ReadableStream === "undefined") {
    global.ReadableStream = ReadableStream;
}

const {width, height} = Dimensions.get('window');

const CHUNK_DURATION = 2500; // 2.5 seconds
const CORE_SERVICE_URL = 'http://10.3.1.29:8000';
const LOCAL_AWS_ENDPOINT = 'http://10.3.1.29:4566';

export default function RecordingScreen() {
    const [isRecording, setIsRecording] = useState(false);
    const [isPaused, setIsPaused] = useState(false);
    const [showQRScanner, setShowQRScanner] = useState(false);
    const [sessionInfo, setSessionInfo] = useState(null);
    const [streamConfig, setStreamConfig] = useState(null);
    const [connectionStatus, setConnectionStatus] = useState('disconnected');
    const [recordingId, setRecordingId] = useState(null);
    const [recordingDuration, setRecordingDuration] = useState(0);
    const [isLoading, setIsLoading] = useState(false);

    const currentPlatform = Platform.OS;
    const recordingRef = useRef(null);
    const lastSentTimestampRef = useRef(0);
    const recordingDurationRef = useRef(0);
    const recordingOptions = {
        ios: {
            extension: '.wav',
            outputFormat: Audio.IOSOutputFormat.LINEARPCM,
            sampleRate: 16000,
            numberOfChannels: 1,
            bitRate: 256000,
            linearPCMBitDepth: 16,
            linearPCMIsBigEndian: false,
        }, android: {
            extension: '.wav',
            outputFormat: Audio.AAC,
            audioEncoder: Audio.AAC_ELD,
            sampleRate: 16000,
            numberOfChannels: 1,
            bitRate: 256000,
        },
    }

    useEffect(() => {
        return () => {
            if (recordingRef.current) {
                stopRecording();
            }
        };
    }, []);

    useEffect(() => {
        let interval;
        if (isRecording && !isPaused) {
            interval = setInterval(() => {
                setRecordingDuration(prev => prev + 1);
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [isRecording, isPaused]);

    const requestMicrophonePermission = async () => {
        const {status} = await Audio.requestPermissionsAsync();
        if (status !== 'granted') {
            Alert.alert('Permission Required', 'Microphone access is needed to record audio.', [{text: 'OK'}]);
            return false;
        }
        return true;
    };

    const initializeRecording = useCallback((sessionInfo, recordingId, streamConfig) => {
        console.log('Initializing recording with:', {sessionInfo, recordingId, streamConfig});
        if (sessionInfo && recordingId && streamConfig) {
            startRecording(sessionInfo, recordingId, streamConfig);
        } else {
            console.error('Failed to initialize recording: missing data', {sessionInfo, recordingId, streamConfig});
            Alert.alert('Error', 'Failed to initialize recording. Please try again.');
        }
    }, []);

    const handleQRScanned = useCallback(async (data) => {
        try {
            console.log('Scanned QR code:', data);

            const scannedData = JSON.parse(data);
            setShowQRScanner(false);
            setIsLoading(true);

            // Pair the device
            const pairResponse = await fetch(`${CORE_SERVICE_URL}/pair`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    sessionId: scannedData.sessionId,
                    token: scannedData.pairingToken,
                }),
                referrerPolicy: "unsafe-url"
            });
            if (!pairResponse.ok) {
                throw new Error('Failed to pair device');
            }

            const pairResult = await pairResponse.json();
            const newStreamConfig = {
                streamName: pairResult.streamUrl.split('/').pop(),
                region: 'us-east-1',
                credentials: {
                    accessKeyId: pairResult.accessKeyId,
                    secretAccessKey: pairResult.secretAccessKey,
                    sessionToken: pairResult.sessionToken,
                }
            };

            // Update state
            setSessionInfo(scannedData);
            setRecordingId(pairResult.recordingId);
            setStreamConfig(newStreamConfig);

            console.log('Device paired successfully');

            // Wait for 5 seconds before starting the recording
            setTimeout(() => {
                setIsLoading(false);
                initializeRecording(scannedData, pairResult.recordingId, newStreamConfig);
            }, 5000);
        } catch (error) {
            console.error('Error handling QR code:', error);
            setSessionInfo(null);
            setStreamConfig(null);
            setRecordingId(null);
            setIsLoading(false);
            Alert.alert('Error', 'Failed to initialize session. Please try again.');
        }
    }, []);

    const startRecording = useCallback(async (sessionInfo, recordingId, streamConfig) => {
        try {
            console.log('Starting recording with sessionInfo:', sessionInfo, 'streamConfig:', streamConfig, 'recordingId:', recordingId);
            if (!sessionInfo || !streamConfig || !recordingId) {
                Alert.alert('Error', 'Session not initialized');
                return;
            }

            const hasPermission = await requestMicrophonePermission();
            if (!hasPermission) {
                return;
            }

            // Notify core service that recording has started
            const utcTimestamp = Math.floor(Date.now() / 1000);
            const startResponse = await fetch(`${CORE_SERVICE_URL}/recording`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    sessionId: sessionInfo.sessionId,
                    recordingId: recordingId,
                    action: 'start',
                    timestamp: utcTimestamp,
                }),
                referrerPolicy: "unsafe-url"
            });
            if (!startResponse.ok) {
                throw new Error('Failed to start recording session');
            }

            const newRecording = new Audio.Recording();

            await Audio.setAudioModeAsync({
                allowsRecordingIOS: true,
                playsInSilentModeIOS: true,
            });
            await newRecording.prepareToRecordAsync(recordingOptions);

            newRecording.setOnRecordingStatusUpdate(status => sendAudioChunk(status, streamConfig, recordingId));
            newRecording.setProgressUpdateInterval(CHUNK_DURATION);
            await newRecording.startAsync();

            recordingRef.current = newRecording;
            setIsRecording(true);
            setIsPaused(false);
            setConnectionStatus('connected');
            lastSentTimestampRef.current = 0;
            recordingDurationRef.current = 0;
            setRecordingDuration(0);

        } catch (err) {
            console.error('Failed to start recording', err);
            Alert.alert('Error', 'Failed to start recording');
        }
    }, []);

    const pauseRecording = useCallback(async () => {
        if (!recordingRef.current || !isRecording || isPaused) return;

        try {
            await recordingRef.current.pauseAsync();
            setIsPaused(true);

            await fetch(`${CORE_SERVICE_URL}/recording`, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json',
                }, body: JSON.stringify({
                    sessionId: sessionInfo.sessionId,
                    recordingId: recordingId,
                    action: 'pause',
                    current_position: recordingDurationRef.current,
                }), referrerPolicy: "unsafe-url"
            });
        } catch (error) {
            console.error('Error pausing recording:', error);
            Alert.alert('Error', 'Failed to pause recording');
        }
    }, [isRecording, isPaused, sessionInfo, recordingId]);

    const resumeRecording = useCallback(async () => {
        if (!recordingRef.current || !isRecording || !isPaused) return;

        try {
            await recordingRef.current.startAsync();
            setIsPaused(false);

            await fetch(`${CORE_SERVICE_URL}/recording`, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json',
                }, body: JSON.stringify({
                    sessionId: sessionInfo.sessionId,
                    recordingId: recordingId,
                    action: 'resume',
                    current_position: recordingDurationRef.current,
                }), referrerPolicy: "unsafe-url"

            });
        } catch (error) {
            console.error('Error resuming recording:', error);
            Alert.alert('Error', 'Failed to resume recording');
        }
    }, [isRecording, isPaused, sessionInfo, recordingId]);

    const stopRecording = useCallback(async () => {
        if (!recordingRef.current) return;

        setIsRecording(false);
        setIsPaused(false);
        try {
            await recordingRef.current.stopAndUnloadAsync();
            // Notify core service that recording has stopped
            await fetch(`${CORE_SERVICE_URL}/recording`, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json',
                }, body: JSON.stringify({
                    sessionId: sessionInfo.sessionId,
                    recordingId: recordingId,
                    action: 'stop',
                    current_position: recordingDurationRef.current,
                }), referrerPolicy: "unsafe-url"

            });

            setStreamConfig(null);
        } catch (error) {
            console.error('Error stopping recording:', error);
        }
        recordingRef.current = null;
        setConnectionStatus('disconnected');
    }, [sessionInfo, recordingId]);

    const sendAudioChunk = useCallback(async (status, streamConfig, recordingId) => {
        const recording = recordingRef.current;
        if (!status.isRecording || !streamConfig || !recording) {
            console.warn('Recording is not active or streamConfig is missing.');
            return;
        }

        recordingDurationRef.current = status.durationMillis;

        try {
            const uri = recording.getURI();
            console.log('Processing audio file from URI:', uri);

            // Get the recording options based on the current platform
            const sampleRate = recordingOptions.ios.sampleRate;  // Assume same settings for both platforms
            const numberOfChannels = recordingOptions.ios.numberOfChannels;
            const bitDepth = 16;  // 16-bit PCM data
            const bytesPerSample = (bitDepth / 8) * numberOfChannels;
            const bytesPerSecond = sampleRate * bytesPerSample;

            // Calculate the start position for the chunk
            const start_position = Math.floor((lastSentTimestampRef.current / 1000) * bytesPerSecond) + 44;  // Skip header

            // Get file info
            const fileInfo = await FileSystem.getInfoAsync(uri);
            const availableBytes = fileInfo.size - start_position;

            // Calculate chunk length, ensuring we don't exceed available bytes
            const chunk_length = Math.min(bytesPerSecond * CHUNK_DURATION / 1000, availableBytes);

            console.log('Reading audio chunk with length:', chunk_length, 'and position:', start_position);

            const chunk = await FileSystem.readAsStringAsync(uri, {
                encoding: FileSystem.EncodingType.Base64, length: chunk_length, position: start_position,
            });

            const kinesisClient = new KinesisClient({
                endpoint: LOCAL_AWS_ENDPOINT,  // Use localstack endpoint
                region: streamConfig.region,  // Use the region from streamConfig
                credentials: streamConfig.credentials,  // Directly use the credentials obtained during pairing
                runtime: 'react-native',  // Explicitly set the runtime
            });

            console.log('Sending audio chunk to Kinesis with the following details:', {
                streamName: streamConfig.streamName, partitionKey: recordingId, chunkSize: chunk.length,
            });

            const command = new PutRecordCommand({
                Data: chunk,  // Send as Base64
                StreamName: streamConfig.streamName, PartitionKey: recordingId,
            });

            await kinesisClient.send(command);

            // Update the timestamp based on the actual amount of data sent
            const sentSeconds = chunk_length / bytesPerSecond;
            lastSentTimestampRef.current += sentSeconds * 1000;  // Convert to milliseconds

            setConnectionStatus('connected');
        } catch (error) {
            console.error('Error sending audio chunk:', error);
            setConnectionStatus('error');
            // Implement retry logic here if needed
        }
    }, [streamConfig, recordingId]);

    return (<View style={styles.container}>
        {showQRScanner ? (<View style={styles.qrScannerContainer}>
            <QRScanner onScanned={handleQRScanned}/>
            <TouchableOpacity
                style={styles.closeButton}
                onPress={() => setShowQRScanner(false)}
            >
                <Text style={styles.closeButtonText}>Close</Text>
            </TouchableOpacity>
        </View>) : isLoading ? (<View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#0000ff"/>
            <Text style={styles.loadingText}>Initializing session...</Text>
        </View>) : (<View style={styles.contentContainer}>
            <Text style={styles.statusText}>Status: {connectionStatus}</Text>
            <Text style={styles.durationText}>
                Recording Duration: {recordingDuration}s
            </Text>
            <View style={styles.buttonContainer}>
                {isRecording && !isPaused && (<TouchableOpacity
                    style={[styles.button, styles.pauseButton]}
                    onPress={pauseRecording}
                >
                    <Pause color="white" size={24}/>
                    <Text style={styles.buttonText}>Pause</Text>
                </TouchableOpacity>)}
                {isRecording && isPaused && (<TouchableOpacity
                    style={[styles.button, styles.resumeButton]}
                    onPress={resumeRecording}
                >
                    <Play color="white" size={24}/>
                    <Text style={styles.buttonText}>Resume</Text>
                </TouchableOpacity>)}
                {isRecording && (<TouchableOpacity
                    style={[styles.button, styles.stopButton]}
                    onPress={stopRecording}
                >
                    <Square color="white" size={24}/>
                    <Text style={styles.buttonText}>Complete</Text>
                </TouchableOpacity>)}
            </View>
            {!isRecording && (<TouchableOpacity
                style={[styles.button, styles.scanButton]}
                onPress={() => setShowQRScanner(true)}
            >
                <Camera color="white" size={24}/>
                <Text style={styles.buttonText}>Scan QR Code</Text>
            </TouchableOpacity>)}
            {sessionInfo && (<Text style={styles.sessionInfo}>Session ID: {sessionInfo.sessionId}</Text>)}
        </View>)}
    </View>);
}

const styles = StyleSheet.create({
    container: {
        flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#f0f0f0',
    }, qrScannerContainer: {
        width: width, height: height, justifyContent: 'center', alignItems: 'center',
    }, contentContainer: {
        width: width * 0.9, padding: 20, backgroundColor: 'white', borderRadius: 10, alignItems: 'center',
    }, loadingContainer: {
        flex: 1, justifyContent: 'center', alignItems: 'center',
    }, loadingText: {
        marginTop: 10, fontSize: 16,
    }, statusText: {
        fontSize: 18, marginBottom: 10,
    }, durationText: {
        fontSize: 16, marginBottom: 20,
    }, buttonContainer: {
        flexDirection: 'row', justifyContent: 'center', marginBottom: 20,
    }, button: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 10,
        borderRadius: 5,
        marginHorizontal: 5,
    }, startButton: {
        backgroundColor: '#4CAF50',
    }, pauseButton: {
        backgroundColor: '#FFA500',
    }, resumeButton: {
        backgroundColor: '#4CAF50',
    }, stopButton: {
        backgroundColor: '#f44336',
    }, scanButton: {
        backgroundColor: '#2196F3',
    }, buttonText: {
        color: 'white', marginLeft: 5,
    }, sessionInfo: {
        marginTop: 20, fontSize: 16,
    }, closeButton: {
        position: 'absolute', top: 40, right: 20, padding: 10, backgroundColor: 'rgba(0, 0, 0, 0.5)', borderRadius: 5,
    }, closeButtonText: {
        color: 'white', fontSize: 16,
    },
});