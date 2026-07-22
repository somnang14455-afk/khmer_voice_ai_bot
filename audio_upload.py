"""
Khmer AI Studio
Audio Upload Module
Version 1.0
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ==========================================
# AUDIO UPLOAD MENU
# ==========================================

def audio_upload_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📂 Import MP3 / Audio",
                callback_data="import_audio"
            )
        ],

        [
            InlineKeyboardButton(
                "🎙️ Record Voice",
                callback_data="record_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 My Voice Profile",
                callback_data="my_voice_profile"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="voice_select"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)