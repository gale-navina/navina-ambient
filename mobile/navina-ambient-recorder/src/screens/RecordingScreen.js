import React, {useState, useEffect, useCallback, useRef} from 'react';
import {View, Text, StyleSheet, Alert, SafeAreaView} from 'react-native';
import {Pause, Play, Square} from 'lucide-react-native';
import {colors} from '../styles/colors';
import {globalStyles} from '../styles/globalStyles';
import RecordingIndicator from '../components/RecordingIndicator';
import ControlButton from '../components/ControlButton';
import {LinearGradient} from 'expo-linear-gradient';
import {
    startRecording,
    pauseRecording,
    resumeRecording,
    stopRecording,
    getRecordingDuration,
    getCurrentTimestamp
} from '../services/audioRecording';
import {notifyRecordingStatus} from '../services/api';
import {formatTime} from '../utils/timeFormatter';

const RecordingScreen = ({navigation, route}) => {
    const [isRecording, setIsRecording] = useState(false);
    const [isPaused, setIsPaused] = useState(false);
    const [recordingDuration, setRecordingDuration] = useState(0);
    const [connectionStatus, setConnectionStatus] = useState('disconnected');
    const {sessionInfo, recordingId, streamConfig} = route.params;
    const recordingIndicatorRef = useRef(null);

    useEffect(() => {
        const initializeRecording = async () => {
            const success = await startRecording(sessionInfo, recordingId, streamConfig);
            if (success) {
                setIsRecording(true);
                setConnectionStatus('connected');
                notifyRecordingStatus(sessionInfo.sessionId, recordingId, 'start', getCurrentTimestamp());
            } else {
                Alert.alert('Error', 'Failed to start recording. Please try again.');
                navigation.goBack();
            }
        };

        initializeRecording();

        return () => {
            stopRecording();
        };
    }, []);

    useEffect(() => {
        let interval;
        if (isRecording && !isPaused) {
            interval = setInterval(() => {
                setRecordingDuration(getRecordingDuration());
                // Simulate amplitude update (replace with real amplitude data later)
                if (recordingIndicatorRef.current) {
                    recordingIndicatorRef.current.updateAmplitude(Math.random());
                }
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [isRecording, isPaused]);

    const handlePauseResume = useCallback(async () => {
        if (isPaused) {
            await resumeRecording();
            setIsPaused(false);
            notifyRecordingStatus(sessionInfo.sessionId, recordingId, 'resume', getCurrentTimestamp());
        } else {
            await pauseRecording();
            setIsPaused(true);
            notifyRecordingStatus(sessionInfo.sessionId, recordingId, 'pause', getCurrentTimestamp());
        }
    }, [isPaused, sessionInfo, recordingId]);

    const handleStop = useCallback(async () => {
        await stopRecording();
        notifyRecordingStatus(sessionInfo.sessionId, recordingId, 'stop', getCurrentTimestamp());
        setConnectionStatus('disconnected');
        navigation.replace('Summary', {duration: recordingDuration});
    }, [recordingDuration, navigation, sessionInfo, recordingId]);

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