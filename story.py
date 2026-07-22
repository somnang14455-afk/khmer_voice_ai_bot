# ==========================================
# Khmer AI Studio
# File : modules/story.py
# Version : 5.3
# Module : Story Studio Navigation Ready
# ==========================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from modules.navigation import back_home_buttons


# ==========================================
# STORY MENU
# ==========================================

def story_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "✍️ Story Generator",
                callback_data="story_generator"
            )
        ],

        [
            InlineKeyboardButton(
                "📝 Script Writer",
                callback_data="script_writer"
            )
        ],

        [
            InlineKeyboardButton(
                "🎭 Character Builder",
                callback_data="character_builder"
            )
        ],

        [
            InlineKeyboardButton(
                "🌍 Story Ideas",
                callback_data="story_ideas"
            )
        ],

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



# ==========================================
# STORY GENERATOR MENU
# ==========================================

def story_generator_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📝 Create Story",
                callback_data="create_story"
            )
        ],

        [
            InlineKeyboardButton(
                "📖 Story Outline",
                callback_data="story_outline"
            )
        ],

        [
            InlineKeyboardButton(
                "🎭 Character Setup",
                callback_data="character_setup"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="story"
            ),

            InlineKeyboardButton(
                "🏠 Home",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)