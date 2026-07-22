"""
Khmer AI Studio
Voice Settings Core System
Version 1.0
"""


# ==========================================
# DEFAULT VOICE SETTINGS
# ==========================================

DEFAULT_SETTINGS = {

    "speed": 1.0,

    "pitch": 1.0,

    "volume": 1.0,

    "style": "normal"

}


# ==========================================
# CREATE VOICE SETTINGS
# ==========================================

def create_settings(
    speed=1.0,
    pitch=1.0,
    volume=1.0,
    style="normal"
):

    return {

        "speed": speed,

        "pitch": pitch,

        "volume": volume,

        "style": style

    }



# ==========================================
# GET DEFAULT SETTINGS
# ==========================================

def get_default_settings():

    return DEFAULT_SETTINGS.copy()



# ==========================================
# UPDATE SETTINGS
# ==========================================

def update_settings(
    settings,
    key,
    value
):

    if key in settings:

        settings[key] = value


    return settings



# ==========================================
# VOICE STYLES
# ==========================================

VOICE_STYLES = {

    "normal": "សំឡេងធម្មតា",

    "narration": "សំឡេងនិទានរឿង",

    "movie": "សំឡេងភាពយន្ត",

    "podcast": "សំឡេង Podcast",

    "advertisement": "សំឡេងផ្សព្វផ្សាយ"

}



def get_voice_styles():

    return VOICE_STYLES