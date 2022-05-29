import React, { useState, useEffect } from 'react'
import Switch from '../Switch/Switch'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

export default function Home() {

    SpeechRecognition.startListening({ continuous: true })
    const [value, setValue] = useState(window.homevalue)
    let Message = ''

    const processCommand = (command) => {
        if (command === 'I am going out') {
            setValue(false);
            window.homevalue = false
            Message = "Have a safe trip"
            window.speechSynthesis.speak(new SpeechSynthesisUtterance(Message))
        }
        if (command === 'I am home') {
            setValue(true);
            window.homevalue = true
            Message = "Welcome Back"
            window.speechSynthesis.speak(new SpeechSynthesisUtterance(Message))

        }
    }

    const commands = [
        {
            command: 'Lulu *',
            callback: (command) => processCommand(command)

        },
    ]

    const {
        transcript,
        resetTranscript,
        browserSupportsSpeechRecognition,
        listening
    } = useSpeechRecognition({ commands });

    console.log(transcript)

    if (!browserSupportsSpeechRecognition) {
        return <span>Browser doesn't support speech recognition.</span>;
    }

    return (
        <div>
            <div className="container">
                <Switch className="toggle-switch"
                    isOn={value}
                    handleToggle={() => {
                        setValue(!value)
                        window.homevalue = !value
                    }}
                />
            </div>
        </div >
    )
}

