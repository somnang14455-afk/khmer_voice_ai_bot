"""
Khmer AI Studio
Emotion Control Module
Version 1.0
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ==========================================
# EMOTION MENU
# ==========================================

def emotion_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "😊 សប្បាយ / រីករាយ",
                callback_data="emotion_happy"
            )
        ],

        [
            InlineKeyboardButton(
                "😢 សោកសៅ / ឈឺចាប់",
                callback_data="emotion_sad"
            )
        ],

        [
            InlineKeyboardButton(
                "😡 ខឹង / ស្រែក",
                callback_data="emotion_angry"
            )
        ],

        [
            InlineKeyboardButton(
                "😱 ភ័យខ្លាច",
                callback_data="emotion_fear"
            )
        ],

        [
            InlineKeyboardButton(
                "🤫 ខ្សឹប",
                callback_data="emotion_whisper"
            )
        ],

        [
            InlineKeyboardButton(
                "😂 កំប្លែង",
                callback_data="emotion_funny"
            )
        ],

        [
            InlineKeyboardButton(
                "🎙️ Normal",
                callback_data="emotion_normal"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="text_to_voice"
            ),

            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)