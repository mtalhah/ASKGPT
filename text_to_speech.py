import pyttsx3
from pygame import mixer
import os
# Initialize the text-to-speech engine
engine = pyttsx3.init()
mixer.init()

voices = engine.getProperty('voices')  
# Set properties (optional)
# You can customize the voice and rate of speech
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.setProperty('rate', 135)  # Speed of speech (words per minute)

def process_text(text):
    # Speak the provided text
    try:
        os.remove("speech.wav")
    finally:
        engine.save_to_file(text, "speech.wav")
        engine.runAndWait()
        print('speech done')

