"""
Khmer AI Studio
Text To Speech Engine
Version 1.0
"""

import os
from gtts import gTTS


# ==========================================
# AUDIO FOLDER
# ==========================================

AUDIO_FOLDER = "profiles/audio"


# ==========================================
# CREATE AUDIO FOLDER
# ==========================================

def create_audio_folder():

    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)



# ==========================================
# TEXT TO MP3
# ==========================================

def text_to_mp3(
    text,
    language="km"
):

    create_audio_folder()


    filename = "voice_output.mp3"


    filepath = os.path.join(
        AUDIO_FOLDER,
        filename
    )


    tts = gTTS(
        text=text,
        lang=language
    )


    tts.save(filepath)


    return filepath
    
    # ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    file = text_to_mp3(
        "សួស្តី Khmer AI Studio"
    )

    print("Audio Created:")
    print(file)
    