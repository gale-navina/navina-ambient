import React, {useState, useEffect, useCallback} from 'react';
import {Text, View, StyleSheet, TouchableOpacity, Platform, Dimensions, Alert, SafeAreaView} from 'react-native';
import {CameraView, Camera} from 'expo-camera';
import {colors} from '../styles/colors';
import {globalStyles} from '../styles/globalStyles';
import {LinearGradient} from 'expo-linear-gradient';
import {pairDevice} from "../services/api";

const {width, height} = Dimensions.get('window');

export default function QRScanner({navigation}) {
    const [hasPermission, setHasPermission] = useState(null);
    const [scanned, setScanned] = useState(false);

    useEffect(() => {
        (async () => {
            const {status} = await Camera.requestCameraPermissionsAsync();
            setHasPermission(status === "granted");
        })();
    }, []);

    const handleBarCodeScanned = (async ({type, data}) => {
        try {
            console.log("Scanned QR code");
            const scannedData = JSON.parse(data);
            setScanned(true);
            const pair_response = await pairDevice(scannedData.sessionId, scannedData.pairingToken);
            if (!pair_response) {
                console.log("Error pairing device");
                return;
            }
            const newStreamConfig = {
                streamName: pair_response.streamUrl.split('/').pop(),
                region: 'us-east-1',
                credentials: {
                    accessKeyId: pair_response.accessKeyId,
                    secretAccessKey: pair_response.secretAccessKey,
                    sessionToken: pair_response.sessionToken,
                }
            };
            const navigation_data = {
                sessionInfo: scannedData,
                recordingId: pair_response.recordingId,
                streamConfig: newStreamConfig

            }
            navigation.navigate('Recording', navigation_data);
        } catch (error) {
            console.error('Error handling QR code:', error);
            Alert.alert('Error', 'Failed to initialize session. Please try again.');
        }
    });

    if (hasPermission === null) {
        return <Text style={globalStyles.subtitle}>Requesting camera permission</Text>;
    }
    if (hasPermission === false) {
        return <Text style={globalStyles.errorText}>No access to camera</Text>;
    }

    return (
        <SafeAreaView style={styles.safeArea}>
            <LinearGradient
                colors={[colors.primary, colors.secondary]}
                style={styles.gradient}
            >
                <View style={styles.container}>
                    {Platform.OS === 'ios' ? (
                        <View style={styles.cameraContainer}>
                            <CameraView
                                style={styles.camera}
                                type="back"
                                onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
                                barcodeScannerSettings={{
                                    barcodeTypes: ['qr'],
                                }}
                            />
                        </View>
                    ) : (
                        <Text style={styles.errorText}>QR scanning is not supported on Android</Text>
                    )}
                    {scanned && (
                        <TouchableOpacity
                            style={styles.button}
                            onPress={() => setScanned(false)}
                        >
                            <Text style={styles.buttonText}>Tap to Scan Again</Text>
                        </TouchableOpacity>
                    )}
                </View>
            </LinearGradient>
        </SafeAreaView>
    );
}

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
    cameraContainer: {
        width: width * 0.8,
        height: width * 0.8,
        overflow: 'hidden',
        borderRadius: 20,
        marginBottom: 30,
    },
    camera: {
        flex: 1,
    },
    errorText: {
        color: colors.white,
        fontSize: 18,
        textAlign: 'center',
    },
    button: {
        backgroundColor: colors.white,
        paddingVertical: 15,
        paddingHorizontal: 30,
        borderRadius: 30,
    },
    buttonText: {
        color: colors.primary,
        fontSize: 18,
        fontWeight: 'bold',
    },
});