"""
Khmer AI Studio
Menu System
Version 5.5 Fixed
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# ==========================================
# HOME PAGE
# ==========================================

def home_page():

    keyboard = [

        [
            InlineKeyboardButton(
                "☰ Menu",
                callback_data="open_menu"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# ==========================================
# FULL MAIN MENU
# ==========================================

def full_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🎙️ Voice Studio",
                callback_data="voice"
            )
        ],

        [
            InlineKeyboardButton(
                "🎬 Story Studio",
                callback_data="story"
            )
        ],

        [
            InlineKeyboardButton(
                "🎥 Video Studio",
                callback_data="video"
            )
        ],

        [
            InlineKeyboardButton(
                "🤖 AI Tools",
                callback_data="ai"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Account",
                callback_data="account"
            ),

            InlineKeyboardButton(
                "💳 Subscription",
                callback_data="subscription"
            )
        ],

        [
            InlineKeyboardButton(
                "⚙️ Settings",
                callback_data="settings"
            ),

            InlineKeyboardButton(
                "ℹ️ About",
                callback_data="about"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# ==========================================
# BACK HOME
# ==========================================

def back_home():

    keyboard = [

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="open_menu"
            ),

            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)