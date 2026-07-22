"""
Khmer AI Studio
Voice Studio Module
Version 1.1
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# ==========================================
# VOICE STUDIO MENU
# ==========================================

def voice_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📖 Text To Voice",
                callback_data="text_to_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "📝 Script To Voice",
                callback_data="script_to_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "🎬 SRT To Voice",
                callback_data="srt_to_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "🎤 Voice Clone",
                callback_data="voice_clone"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Voice Profile",
                callback_data="voice_profile"
            )
        ],

        [
            InlineKeyboardButton(
                "😊 Emotion Voice",
                callback_data="emotion_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "⚙️ Voice Settings",
                callback_data="voice_settings"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="open_menu"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)