import React from 'react';
import {TouchableOpacity, Text, StyleSheet} from 'react-native';
import {colors} from '../styles/colors';

const ControlButton = ({onPress, icon: Icon, text, color, textColor, style}) => {
    return (
        <TouchableOpacity
            style={[styles.button, {backgroundColor: color}, style]}
            onPress={onPress}
        >
            <Icon color={textColor || colors.white} size={24}/>
            <Text style={[styles.buttonText, {color: textColor || colors.white}]}>{text}</Text>
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    button: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingVertical: 15,
        paddingHorizontal: 30,
        borderRadius: 30,
        marginHorizontal: 10,
        elevation: 5,
        shadowColor: colors.dark,
        shadowOffset: {width: 0, height: 2},
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
    },
    buttonText: {
        fontSize: 18,
        fontWeight: 'bold',
        marginLeft: 10,
    },
});

export default ControlButton;