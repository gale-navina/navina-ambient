import React, {useState, useEffect, useCallback, useRef} from 'react';
import {View, Text, StyleSheet, Alert, SafeAreaView} from 'react-native';
import {Pause, Play, Square} from 'lucide-react-native';
import {colors} from '../styles/colors';
import {globalStyles} from '../styles/globalStyles';
import RecordingIndicator from '../components/RecordingIndicator';
import ControlButton from '../components/ControlButton';
import {LinearGradient} from 'expo-linear-gradient';
import RecordingManager from '../services/audioRecording'; // Updated import
import {notifyRecordingStatus} from '../services/api';
import {formatTime} from '../utils/timeFormatter';

const RecordingScreen = ({navigation, route}) => {
    const [isRecording, setIsRecording] = useState(false);
    const [isPaused, setIsPaused] = useState(false);
    const [recordingDuration, setRecordingDuration] = useState(0);
    const [connectionStatus, setConnectionStatus] = useState('disconnected');
    const {sessionInfo, recordingId, streamConfig} = route.params;
    const recordingIndicatorRef = useRef(null);
    const intervalRef = useRef(null);

    // Reference to the RecordingManager instance
    const recordingManagerRef = useRef(null);

    useEffect(() => {
        const initializeRecording = async () => {
            const manager = new RecordingManager(streamConfig, recordingId);
            recordingManagerRef.current = manager;

            const success = await manager.startRecording();
            if (success) {
                setIsRecording(true);
                setConnectionStatus('connected');
                notifyRecordingStatus(sessionInfo.sessionId, recordingId, 'start', manager.getCurrentTimestamp());
                startDurationUpdate();
            } else {
                Alert.alert('Error', 'Failed to start recording. Please try again.');
                navigation.goBack();
            }
        };

        initializeRecording();

        return () => {
            if (recordingManagerRef.current) {
                recordingManagerRef.current.stopRecording();
            }
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, []);

    const normalizeAmplitude = (db) => {
        const minDb = -30;  // Quiet environment
        const maxDb = -10;  // Loud sound (adjust if needed)
        const clampedDb = Math.min(Math.max(db, minDb), maxDb);
        return (clampedDb - minDb) / (maxDb - minDb);
    };

    const handlePauseResume = useCallback(async () => {
        if (!recordingManagerRef.current) return;

        if (isPaused) {
            await recordingManagerRef.current.resume(); // Await resume()
            setIsPaused(false);
            notifyRecordingStatus(
                sessionInfo.sessionId,
                recordingId,
                'resume',
                recordingManagerRef.current.getCurrentTimestamp()
            );
        } else {
            await recordingManagerRef.current.pause(); // Await pause()
            setIsPaused(true);
            notifyRecordingStatus(
                sessionInfo.sessionId,
                recordingId,
                'pause',
                recordingManagerRef.current.getCurrentTimestamp()
            );
        }
    }, [isPaused, sessionInfo, recordingId]);

    const handleStop = useCallback(async () => {
        if (!recordingManagerRef.current) return;

        await recordingManagerRef.current.stopRecording();
        notifyRecordingStatus(
            sessionInfo.sessionId,
            recordingId,
            'stop',
            recordingManagerRef.current.getCurrentTimestamp()
        );
        setConnectionStatus('disconnected');
        if (intervalRef.current) {
            clearInterval(intervalRef.current);
        }
        navigation.replace('Summary', {duration: Math.floor(recordingDuration / 1000)});
    }, [recordingDuration, navigation, sessionInfo, recordingId]);

    const startDurationUpdate = () => {
        intervalRef.current = setInterval(async () => {
            try {
                const status = await recordingManagerRef.current.getRecordingStatus();
                if (status) {
                    setRecordingDuration(status.durationMillis);
                    if (recordingIndicatorRef.current && status.metering !== undefined) {
                        let normalizedAmplitude = normalizeAmplitude(status.metering);
                        normalizedAmplitude = Math.pow(normalizedAmplitude, 0.5);

                        recordingIndicatorRef.current.updateAmplitude(normalizedAmplitude);
                    }
                }
            } catch (error) {
                console.error('Error in startDurationUpdate:', error);
            }
        }, 250); // Update UI every 250ms
    };

    return (
        <SafeAreaView style={styles.safeArea}>
            <LinearGradient
                colors={[colors.primary, colors.secondary]}
                style={styles.gradient}
            >
                <View style={styles.container}>
                    <RecordingIndicator
                        ref={recordingIndicatorRef}
                        isRecording={isRecording}
                        isPaused={isPaused}
                    />
                    <Text style={styles.durationText}>{formatTime(Math.floor(recordingDuration / 1000))}</Text>
                    <Text style={styles.statusText}>Status: {connectionStatus}</Text>
                    <View style={styles.controlsContainer}>
                        <ControlButton
                            onPress={handlePauseResume}
                            icon={isPaused ? Play : Pause}
                            text={isPaused ? 'Resume' : 'Pause'}
                            color={colors.white}
                            textColor={colors.primary}
                        />
                    </View>
                    <ControlButton
                        onPress={handleStop}
                        icon={Square}
                        text="Complete Recording"
                        color={colors.white}
                        textColor={colors.primary}
                        style={styles.completeButton}
                    />
                </View>
            </LinearGradient>
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    safeArea: {
        flex: 1,
    },
    gradient: {
        flex: 1,
    },
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
    },
    durationText: {
        fontSize: 48,
        fontWeight: 'bold',
        color: colors.white,
        marginVertical: 30,
    },
    statusText: {
        fontSize: 18,
        color: colors.white,
        marginBottom: 20,
    },
    controlsContainer: {
        flexDirection: 'row',
        justifyContent: 'center',
        marginBottom: 50,
    },
    completeButton: {
        position: 'absolute',
        bottom: 40,
    },
});

export default RecordingScreen;
