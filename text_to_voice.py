"""
Khmer AI Studio
Text To Voice Module
Version 6.0
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# ==========================================
# TEXT TO VOICE MENU
# ==========================================

def text_to_voice_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🎤 ជ្រើសសំឡេង",
                callback_data="voice_select"
            )
        ],

        [
            InlineKeyboardButton(
                "😊 ជ្រើស Emotion",
                callback_data="emotion_select"
            )
        ],

        [
            InlineKeyboardButton(
                "🎚️ ល្បឿនអាន",
                callback_data="speed_select"
            )
        ],

        [
            InlineKeyboardButton(
                "📝 ផ្ញើអត្ថបទ",
                callback_data="send_text"
            )
        ],

        [
            InlineKeyboardButton(
                "⚙️ AI បង្កើតសំឡេង",
                callback_data="generate_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="voice"
            ),

            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )
        ]

    ]


    return InlineKeyboardMarkup(keyboard)