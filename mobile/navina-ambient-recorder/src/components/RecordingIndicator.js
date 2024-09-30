import React, {useEffect, useRef, useState, forwardRef, useImperativeHandle} from 'react';
import {View, StyleSheet, Animated} from 'react-native';
import {Mic, MicOff} from 'lucide-react-native';
import {colors} from '../styles/colors';

const RecordingIndicator = forwardRef(({isRecording, isPaused}, ref) => {
    const [amplitude, setAmplitude] = useState(0);
    const outerCircleAnim = useRef(new Animated.Value(1)).current;
    const middleCircleAnim = useRef(new Animated.Value(1)).current;
    const opacityAnim = useRef(new Animated.Value(0.5)).current;

    useImperativeHandle(ref, () => ({
        updateAmplitude: (newAmplitude) => {
            setAmplitude(Math.max(0, Math.min(1, newAmplitude)));
        }
    }));

    useEffect(() => {
        if (isRecording && !isPaused) {
            // Animate outer circle based on full amplitude
            Animated.spring(outerCircleAnim, {
                toValue: 1 + amplitude * 0.5, // Max 50% larger
                friction: 5,
                tension: 40,
                useNativeDriver: true,
            }).start();

            // Animate middle circle to a random size between inner and max amplitude
            const randomScale = 1 + Math.random() * amplitude * 0.5;
            Animated.spring(middleCircleAnim, {
                toValue: randomScale,
                friction: 5,
                tension: 40,
                useNativeDriver: true,
            }).start();
        } else {
            // Reset animations when not recording
            Animated.parallel([
                Animated.spring(outerCircleAnim, {
                    toValue: 1,
                    friction: 3,
                    tension: 40,
                    useNativeDriver: true,
                }),
                Animated.spring(middleCircleAnim, {
                    toValue: 1,
                    friction: 3,
                    tension: 40,
                    useNativeDriver: true,
                }),
            ]).start();
        }
    }, [isRecording, isPaused, amplitude]);

    const innerCircleSize = 120; // Base size of the circles

    return (
        <View style={styles.container}>
            <Animated.View
                style={[
                    styles.outerCircle,
                    {
                        width: innerCircleSize,
                        height: innerCircleSize,
                        transform: [{scale: outerCircleAnim}],
                        opacity: opacityAnim,
                    },
                ]}
            />
            <Animated.View
                style={[
                    styles.middleCircle,
                    {
                        width: innerCircleSize,
                        height: innerCircleSize,
                        transform: [{scale: middleCircleAnim}],
                        opacity: opacityAnim,
                    },
                ]}
            />
            <View style={[styles.innerCircle, {width: innerCircleSize, height: innerCircleSize}]}>
                {isRecording && !isPaused ? (
                    <Mic color={colors.primary} size={48}/>
                ) : (
                    <MicOff color={colors.primary} size={48}/>
                )}
            </View>
        </View>
    );
});

const styles = StyleSheet.create({
    container: {
        alignItems: 'center',
        justifyContent: 'center',
        width: 200,
        height: 200,
    },
    outerCircle: {
        position: 'absolute',
        borderRadius: 60,
        backgroundColor: colors.white,
    },
    middleCircle: {
        position: 'absolute',
        borderRadius: 60,
        backgroundColor: colors.white,
    },
    innerCircle: {
        borderRadius: 60,
        backgroundColor: colors.white,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default RecordingIndicator;