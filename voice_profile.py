"""
Khmer AI Studio
Voice Profile Core System
Version 1.0
"""

import json
import os


PROFILE_FILE = "profiles/voice_profiles.json"


# ==========================================
# CREATE PROFILE FOLDER
# ==========================================

def create_storage():

    folder = os.path.dirname(PROFILE_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(PROFILE_FILE):

        with open(PROFILE_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)



# ==========================================
# LOAD VOICE PROFILES
# ==========================================

def load_profiles():

    create_storage()

    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# ==========================================
# SAVE VOICE PROFILES
# ==========================================

def save_profiles(profiles):

    create_storage()

    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profiles,
            file,
            ensure_ascii=False,
            indent=4
        )



# ==========================================
# ADD NEW VOICE PROFILE
# ==========================================

def add_profile(
    name,
    voice_type="Unknown",
    language="Khmer",
    style="Normal",
    clone=False
):

    profiles = load_profiles()


    new_profile = {

        "name": name,
        "voice_type": voice_type,
        "language": language,
        "style": style,
        "clone_voice": clone

    }


    profiles.append(new_profile)

    save_profiles(profiles)


    return new_profile



# ==========================================
# GET ALL PROFILES
# ==========================================

def get_profiles():

    return load_profiles()



# ==========================================
# FIND PROFILE
# ==========================================

def get_profile(name):

    profiles = load_profiles()


    for profile in profiles:

        if profile["name"] == name:

            return profile


    return None