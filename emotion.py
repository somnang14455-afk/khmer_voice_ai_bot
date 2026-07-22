"""
Khmer AI Studio
Emotion Core System
Version 1.0
"""


# ==========================================
# AVAILABLE EMOTIONS
# ==========================================

EMOTIONS = {

    "normal": {
        "name": "😐 Normal",
        "description": "សំឡេងធម្មតា ស្មើ"
    },


    "happy": {
        "name": "😀 Happy",
        "description": "សំឡេងរីករាយ សប្បាយចិត្ត"
    },


    "sad": {
        "name": "😢 Sad",
        "description": "សំឡេងកម្សត់ ឈឺចាប់"
    },


    "angry": {
        "name": "😡 Angry",
        "description": "សំឡេងខឹង ខ្លាំង"
    },


    "fear": {
        "name": "😨 Fear",
        "description": "សំឡេងភ័យខ្លាច"
    },


    "story": {
        "name": "🎬 Story",
        "description": "សំឡេងនិទានរឿង"
    },


    "advertisement": {
        "name": "📢 Advertisement",
        "description": "សំឡេងផ្សព្វផ្សាយ"
    }

}


# ==========================================
# GET ALL EMOTIONS
# ==========================================

def get_emotions():

    return EMOTIONS



# ==========================================
# GET ONE EMOTION
# ==========================================

def get_emotion(emotion_id):

    return EMOTIONS.get(emotion_id)



# ==========================================
# CHECK EMOTION
# ==========================================

def is_valid_emotion(emotion_id):

    return emotion_id in EMOTIONS