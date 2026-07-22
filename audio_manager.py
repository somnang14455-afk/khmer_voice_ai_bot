"""
Khmer AI Studio
Audio Manager Core System
Version 1.0
"""

import os
import shutil


# ==========================================
# AUDIO STORAGE
# ==========================================

AUDIO_FOLDER = "profiles/audio"


# ==========================================
# CREATE AUDIO FOLDER
# ==========================================

def create_audio_storage():

    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)



# ==========================================
# SAVE AUDIO FILE
# ==========================================

def save_audio(
    source_file,
    filename
):

    create_audio_storage()

    destination = os.path.join(
        AUDIO_FOLDER,
        filename
    )

    shutil.copy(
        source_file,
        destination
    )

    return destination



# ==========================================
# GET AUDIO FILES
# ==========================================

def get_audio_files():

    create_audio_storage()

    files = []

    for file in os.listdir(AUDIO_FOLDER):

        files.append(file)

    return files



# ==========================================
# DELETE AUDIO FILE
# ==========================================

def delete_audio(filename):

    path = os.path.join(
        AUDIO_FOLDER,
        filename
    )

    if os.path.exists(path):

        os.remove(path)

        return True


    return False