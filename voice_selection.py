# ==========================================
# Khmer AI Studio
# Voice Selection Module
# Version 6.0
# ==========================================


from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# ==========================================
# VOICE SELECTION MENU
# ==========================================

def voice_selection_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "👨 សំឡេងប្រុស",
                callback_data="male_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "👩 សំឡេងស្រី",
                callback_data="female_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "👴 សំឡេងចាស់",
                callback_data="old_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "👧 សំឡេងក្មេង",
                callback_data="young_voice"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Voice Clone Profile",
                callback_data="clone_voice"
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