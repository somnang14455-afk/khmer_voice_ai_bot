# ==========================================
# Khmer AI Studio
# File : main.py
# Version : 5.7 Clean
# ==========================================


from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


from config import BOT_TOKEN


# ==========================================
# MENU MODULE
# ==========================================

from modules.menu import (
    home_page,
    full_menu,
)


# ==========================================
# NAVIGATION
# ==========================================

from modules.nav_controller import (
    navigation,
)


# ==========================================
# VOICE MODULE
# ==========================================

from modules.voice import (
    voice_menu,
)


# ==========================================
# TEXT TO VOICE
# ==========================================

from modules.text_to_voice import (
    text_to_voice_menu,
)


# ==========================================
# VOICE SELECTION
# ==========================================

from modules.voice_selection import (
    voice_selection_menu,
)


# ==========================================
# TEXT INPUT
# ==========================================

from modules.text_input import (
    start_text_input,
)
from modules.text_handler import (
    handle_text,
)

# ==========================================
# AUDIO UPLOAD
# ==========================================

from modules.audio_upload import (
    audio_upload_menu,
)


# ==========================================
# STORY
# ==========================================

from modules.story import (
    story_menu,
    story_generator_menu,
)


# ==========================================
# START COMMAND
# ==========================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    navigation.reset()

    await update.message.reply_text(

        text=(
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🇰🇭 Khmer AI Studio\n\n"
            "🎙️ Professional AI Creator\n\n"
            "✨ Voice • Story • Video • AI Tools\n\n"
            "សូមចុច Menu ដើម្បីចាប់ផ្តើម\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
        ),

        reply_markup=home_page()

    )    
    
    # ==========================================
# BUTTON CONTROLLER
# ==========================================

async def buttons(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    try:
        await query.answer()
    except Exception:
        pass


    data = query.data

    print("CALLBACK DATA:", data)


    # ======================================
    # HOME
    # ======================================

    if data == "home":

        navigation.reset()

        await query.edit_message_text(

            text=(
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "🇰🇭 Khmer AI Studio\n\n"
                "🎙️ Professional AI Creator\n\n"
                "✨ Voice • Story • Video • AI Tools\n\n"
                "សូមចុច Menu ដើម្បីចាប់ផ្តើម\n"
                "━━━━━━━━━━━━━━━━━━━━━━"
            ),

            reply_markup=home_page()

        )

        return



    # ======================================
    # MAIN MENU
    # ======================================

    if data == "open_menu":

        await query.edit_message_text(

            text=(
                "☰ Khmer AI Studio Menu\n\n"
                "សូមជ្រើសរើសមុខងារ"
            ),

            reply_markup=full_menu()

        )

        return



    # ======================================
    # VOICE STUDIO
    # ======================================

    if data == "voice":

        await query.edit_message_text(

            text=(
                "🎙️ Voice Studio\n\n"
                "ជ្រើសរើសមុខងារ"
            ),

            reply_markup=voice_menu()

        )

        return



    # ======================================
    # TEXT TO VOICE
    # ======================================

    if data == "text_to_voice":

        await query.edit_message_text(

            text=(
                "📖 Text To Voice\n\n"
                "ជ្រើសរើសជំហានបន្ទាប់"
            ),

            reply_markup=text_to_voice_menu()

        )

        return



    # ======================================
    # VOICE SELECTION
    # ======================================

    if data == "voice_select":

        await query.edit_message_text(

            text=(
                "🎤 Voice Selection\n\n"
                "សូមជ្រើសរើសប្រភេទសំឡេង"
            ),

            reply_markup=voice_selection_menu()

        )

        return



    # ======================================
    # VOICE CHOICE
    # ======================================

    voice_names = {

        "male_voice": "👨 សំឡេងប្រុស",
        "female_voice": "👩 សំឡេងស្រី",
        "old_voice": "👴 សំឡេងចាស់",
        "young_voice": "👧 សំឡេងក្មេង",
        "clone_voice": "👤 Voice Clone"

    }


    if data in voice_names:

        await query.edit_message_text(

            text=(
                "✅ Voice Selected\n\n"
                f"{voice_names[data]}\n\n"
                "អាចបន្តទៅជំហានបន្ទាប់"
            ),

            reply_markup=text_to_voice_menu()

        )

        return
      
      
          # ======================================
    # VOICE CLONE
    # ======================================

    if data == "clone_voice":

        await query.edit_message_text(

            text=(
                "👤 Voice Clone Studio\n\n"
                "ជ្រើសរើសវិធីបញ្ចូលសំឡេង"
            ),

            reply_markup=audio_upload_menu()

        )

        return



    # ======================================
    # SEND TEXT
    # ======================================

    if data in [
    "send_text",
    "script_to_voice"
]:

        start_text_input(
            query.from_user.id
        )

        await query.edit_message_text(

            text=(
                "📝 សូមផ្ញើអត្ថបទមក\n\n"
                "Bot កំពុងរង់ចាំអត្ថបទរបស់អ្នក"
            )

        )

        return



    # ======================================
    # STORY
    # ======================================

    if data == "story":

        await query.edit_message_text(

            text=(
                "🎬 Story Studio\n\n"
                "ជ្រើសរើសមុខងារ"
            ),

            reply_markup=story_menu()

        )

        return



    # ======================================
    # STORY GENERATOR
    # ======================================

    if data == "story_generator":

        await query.edit_message_text(

            text=(
                "✍️ Story Generator\n\n"
                "ជ្រើសរើសមុខងារ"
            ),

            reply_markup=story_generator_menu()

        )

        return



    # ======================================
    # DEFAULT
    # ======================================

    await query.edit_message_text(

        text="🚧 Module Coming Soon",

        reply_markup=home_page()

    )



# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )


    app.add_handler(

        CallbackQueryHandler(
            buttons
        )

    )


    print("==============================")
    print("Khmer AI Studio")
    print("Version 5.7 Clean")
    print("Controller Ready")
    print("==============================")


    app.run_polling()



# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    main()
    
    
    
    