import React from 'react';
import {View, Text, StyleSheet, TouchableOpacity, Image, SafeAreaView} from 'react-native';
import {Camera, FileText, Brain, Clock} from 'lucide-react-native';
import {colors} from '../styles/colors';
import {globalStyles} from '../styles/globalStyles';
import {LinearGradient} from 'expo-linear-gradient';

const MainScreen = ({navigation}) => {
    return (
        <SafeAreaView style={styles.safeArea}>
            <LinearGradient
                colors={[colors.primary, colors.secondary]}
                style={styles.gradient}
            >
                <View style={styles.container}>
                    <View style={styles.header}>
                        <Image
                            source={require('../../assets/adaptive-icon-white.png')}
                            style={styles.logo}
                        />
                        <Text style={styles.title}>Navina</Text>
                        <Text style={styles.subtitle}>AI Medical Assistant</Text>
                    </View>

                    <Text style={styles.tagline}>Your medical scribe, powered by artificial intelligence</Text>

                    <View style={styles.infoContainer}>
                        <View style={styles.infoItem}>
                            <FileText color={colors.white} size={24}/>
                            <Text style={styles.infoText}>Comprehensive Records</Text>
                        </View>
                        <View style={styles.infoItem}>
                            <Brain color={colors.white} size={24}/>
                            <Text style={styles.infoText}>AI-Powered Insights</Text>
                        </View>
                        <View style={styles.infoItem}>
                            <Clock color={colors.white} size={24}/>
                            <Text style={styles.infoText}>Stay Focused, {'\n'} Save Time</Text>
                        </View>
                    </View>

                    <TouchableOpacity
                        style={styles.scanButton}
                        onPress={() => navigation.navigate('QRScanner')}
                    >
                        <Camera color={colors.primary} size={24}/>
                        <Text style={styles.buttonText}>Scan QR Code to Begin</Text>
                    </TouchableOpacity>

                    <Text style={styles.footer}>Focus on patients, let AI handle the paperwork</Text>
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
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: 20,
    },
    header: {
        alignItems: 'center',
        marginTop: 40,
    },
    logo: {
        width: 100,
        height: 100,
        marginBottom: 10,
    },
    title: {
        fontSize: 36,
        fontWeight: 'bold',
        color: colors.white,
        marginBottom: 5,
    },
    subtitle: {
        fontSize: 18,
        color: colors.white,
        opacity: 0.8,
    },
    tagline: {
        fontSize: 16,
        color: colors.white,
        textAlign: 'center',
        marginVertical: 20,
        paddingHorizontal: 20,
    },
    infoContainer: {
        flexDirection: 'row',
        justifyContent: 'space-around',
        width: '100%',
        marginVertical: 30,
    },
    infoItem: {
        alignItems: 'center',
        flex: 1,
    },
    infoText: {
        color: colors.white,
        marginTop: 10,
        textAlign: 'center',
        fontSize: 12,
    },
    scanButton: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: colors.white,
        paddingVertical: 15,
        paddingHorizontal: 30,
        borderRadius: 30,
        elevation: 5,
        shadowColor: colors.dark,
        shadowOffset: {width: 0, height: 2},
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
    },
    buttonText: {
        color: colors.primary,
        fontSize: 18,
        fontWeight: 'bold',
        marginLeft: 10,
    },
    footer: {
        color: colors.white,
        opacity: 0.8,
        marginBottom: 20,
        textAlign: 'center',
    },
});

export default MainScreen;