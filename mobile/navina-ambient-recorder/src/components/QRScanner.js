import React, {useState, useEffect} from 'react';
import {Text, View, StyleSheet, Button, Dimensions, Platform, TextInput} from 'react-native';
import {CameraView, Camera} from 'expo-camera';
import {BarCodeScanner} from 'expo-barcode-scanner';

const {width, height} = Dimensions.get('window');

export default function QRScanner({onScanned}) {
    const [hasPermission, setHasPermission] = useState(null);
    const [scanned, setScanned] = useState(false);
    const [sessionId, setSessionId] = useState('');
    const [pairingToken, setPairingToken] = useState('');


    useEffect(() => {
        const getCameraPermissions = async () => {
            const {status} = await Camera.requestCameraPermissionsAsync();
            setHasPermission(status === "granted");
        };

        getCameraPermissions();
    }, []);

    const handleBarCodeScanned = ({type, data}) => {
        console.log("scanned qr")
        if (scanned) return;
        setScanned(true);
        onScanned(data);
    };

    const handleSubmit = () => {
        console.log("mimic scan qr")
        if (scanned) return;
        setScanned(true);
        const data = JSON.stringify({sessionId, pairingToken});
        onScanned(data);
    };

    if (hasPermission === null) {
        return <Text>Requesting camera permission</Text>;
    }
    if (hasPermission === false) {
        return <Text>No access tio camera</Text>;
    }

    return (
        <View style={styles.container}>
            {Platform.OS === 'ios' ? (
                    <CameraView
                        style={styles.camera}
                        type="back"
                        onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
                        autofocus="on"
                        barcodeScannerSettings={{
                            barcodeTypes: ['qr'],
                        }}
                    />
                )
                : Platform.OS === 'web' ? (
                    <View style={styles.innerContainer}>
                        <TextInput
                            style={styles.input}
                            placeholder="Enter Session ID"
                            value={sessionId}
                            onChangeText={setSessionId}
                        />
                        <TextInput
                            style={styles.input}
                            placeholder="Enter Token"
                            value={pairingToken}
                            onChangeText={setPairingToken}
                            secureTextEntry
                        />
                        <Button title="Submit" onPress={handleSubmit}/>
                    </View>
                ) : (
                    <Text>Platform not supported</Text>
                )}

            {
                scanned && (
                    <Button title={'Tap to Scan Again'} onPress={() => setScanned(false)}/>
                )
            }
        </View>
    )
        ;
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'center',
    },
    innerContainer: {
        width: 200,
        height: 200,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#d3d3d3',
    },
    camera: {
        width: width * 0.8,
        height: width * 0.8,
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 10,
        paddingHorizontal: 10,
    },
});