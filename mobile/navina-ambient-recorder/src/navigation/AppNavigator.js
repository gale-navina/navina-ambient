import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import MainScreen from '../screens/MainScreen';
import QRScanner from '../components/QRScanner';
import RecordingScreen from '../screens/RecordingScreen';
import SummaryScreen from '../screens/SummaryScreen';
import {colors} from '../styles/colors';

const Stack = createStackNavigator();

const AppNavigator = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator
                screenOptions={{
                    headerStyle: {
                        backgroundColor: colors.primary,
                    },
                    headerTintColor: colors.white,
                    headerTitleStyle: {
                        fontWeight: 'bold',
                    },
                }}
            >
                <Stack.Screen
                    name="Main"
                    component={MainScreen}
                    options={{headerShown: false}}
                />
                <Stack.Screen
                    name="QRScanner"
                    component={QRScanner}
                    options={{title: 'Scan QR Code'}}
                />
                <Stack.Screen
                    name="Recording"
                    component={RecordingScreen}
                    options={{title: 'Recording', headerLeft: null}}
                />
                <Stack.Screen
                    name="Summary"
                    component={SummaryScreen}
                    options={{title: 'Recording Summary', headerLeft: null}}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default AppNavigator;