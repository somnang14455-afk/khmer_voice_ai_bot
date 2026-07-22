"""
Khmer AI Studio
Navigation Module
Version 5.4
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# ==========================================
# HOME BUTTON
# ==========================================

def home_button():

    keyboard = [

        [
            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# ==========================================
# BACK + HOME BUTTON
# ==========================================

def back_home_buttons(
    back_callback="open_menu"
):

    keyboard = [

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data=back_callback
            ),

            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# ==========================================
# BACK ONLY
# ==========================================

def back_button(
    back_callback="open_menu"
):

    keyboard = [

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data=back_callback
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)