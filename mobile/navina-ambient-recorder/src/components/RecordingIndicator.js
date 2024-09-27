import React, {useEffect, useRef, useState} from 'react';
import {View, StyleSheet, Animated} from 'react-native';
import {Mic, MicOff} from 'lucide-react-native';
import {colors} from '../styles/colors';

const RecordingIndicator = ({isRecording, isPaused}) => {
    const [amplitude, setAmplitude] = useState(0);
    const pulseAnim1 = useRef(new Animated.Value(1)).current;
    const pulseAnim2 = useRef(new Animated.Value(1)).current;
    const opacityAnim1 = useRef(new Animated.Value(0.5)).current;
    const opacityAnim2 = useRef(new Animated.Value(0.3)).current;

    useEffect(() => {
        let animation;
        let amplitudeInterval;

        if (isRecording && !isPaused) {
            const animateCircle = (anim, maxScale) => {
                const randomDuration = 1500 + Math.random() * 1000; // Random duration between 1.5 and 2.5 seconds
                const randomScale = 1 + (Math.random() * (maxScale - 1) * amplitude);

                return Animated.timing(anim, {
                    toValue: randomScale,
                    duration: randomDuration,
                    useNativeDriver: true,
                });
            };

            const startAnimation = () => {
                animation = Animated.parallel([
                    animateCircle(pulseAnim1, 1.3),
                    animateCircle(pulseAnim2, 1.5),
                ]);
                animation.start((({finished}) => {
                    if (finished) {
                        pulseAnim1.setValue(1);
                        pulseAnim2.setValue(1);
                        startAnimation();
                    }
                }));
            };

            startAnimation();

            // Simulate amplitude changes (replace this with real amplitude data later)
            amplitudeInterval = setInterval(() => {
                setAmplitude(Math.random());
            }, 2000);
        } else {
            pulseAnim1.setValue(1);
            pulseAnim2.setValue(1);
        }

        return () => {
            if (animation) {
                animation.stop();
            }
            if (amplitudeInterval) {
                clearInterval(amplitudeInterval);
            }
        };
    }, [isRecording, isPaused, amplitude, pulseAnim1, pulseAnim2]);

    // Function to update amplitude (to be called from parent component)
    const updateAmplitude = (newAmplitude) => {
        setAmplitude(Math.max(0, Math.min(1, newAmplitude))); // Ensure amplitude is between 0 and 1
    };

    return (
        <View style={styles.container}>
            <Animated.View
                style={[
                    styles.outerCircle,
                    {
                        transform: [{scale: pulseAnim2}],
                        opacity: opacityAnim2,
                    },
                ]}
            />
            <Animated.View
                style={[
                    styles.middleCircle,
                    {
                        transform: [{scale: pulseAnim1}],
                        opacity: opacityAnim1,
                    },
                ]}
            />
            <View style={styles.innerCircle}>
                {isRecording && !isPaused ? (
                    <Mic color={colors.primary} size={48}/>
                ) : (
                    <MicOff color={colors.primary} size={48}/>
                )}
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        alignItems: 'center',
        justifyContent: 'center',
    },
    outerCircle: {
        position: 'absolute',
        width: 150,
        height: 150,
        borderRadius: 75,
        backgroundColor: colors.white,
    },
    middleCircle: {
        position: 'absolute',
        width: 130,
        height: 130,
        borderRadius: 65,
        backgroundColor: colors.white,
    },
    innerCircle: {
        width: 120,
        height: 120,
        borderRadius: 60,
        backgroundColor: colors.white,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default RecordingIndicator;