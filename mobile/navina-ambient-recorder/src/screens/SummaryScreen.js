import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, SafeAreaView } from 'react-native';
import { Check } from 'lucide-react-native';
import { colors } from '../styles/colors';
import { globalStyles } from '../styles/globalStyles';
import { LinearGradient } from 'expo-linear-gradient';
import { formatTime } from '../utils/timeFormatter';

const SummaryScreen = ({ navigation, route }) => {
    const { duration } = route.params;

    return (
        <SafeAreaView style={styles.safeArea}>
            <LinearGradient
                colors={[colors.primary, colors.secondary]}
                style={styles.gradient}
            >
                <View style={styles.container}>
                    <View style={styles.summaryBox}>
                        <Check color={colors.accentGreen} size={64} />
                        <Text style={styles.title}>Recording Complete</Text>
                        <Text style={styles.durationText}>
                            Total Duration: {formatTime(duration)}
                        </Text>
                    </View>
                    <TouchableOpacity
                        style={styles.button}
                        onPress={() => navigation.navigate('Main')}
                    >
                        <Text style={styles.buttonText}>Return to Main Page</Text>
                    </TouchableOpacity>
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
    summaryBox: {
        backgroundColor: colors.white,
        borderRadius: 20,
        padding: 30,
        alignItems: 'center',
        shadowColor: colors.dark,
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        color: colors.primary,
        marginVertical: 20,
    },
    durationText: {
        fontSize: 18,
        color: colors.secondary,
    },
    button: {
        backgroundColor: colors.white,
        paddingVertical: 15,
        paddingHorizontal: 30,
        borderRadius: 30,
        marginTop: 40,
    },
    buttonText: {
        color: colors.primary,
        fontSize: 18,
        fontWeight: 'bold',
    },
});

export default SummaryScreen;