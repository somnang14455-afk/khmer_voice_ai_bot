# ==========================================
# Khmer AI Studio
# Home Module
# Version 4.1
# ==========================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():

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
                callback_data="payment"
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
        ]

    ]

    return InlineKeyboardMarkup(keyboard)