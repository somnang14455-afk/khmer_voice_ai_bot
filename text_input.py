"""
Khmer AI Studio
Text Input Module
Version 1.0
"""

# ==========================================
# TEXT INPUT STATE
# ==========================================

user_waiting_text = set()


# ==========================================
# START TEXT INPUT
# ==========================================

def start_text_input(user_id):

    user_waiting_text.add(user_id)



# ==========================================
# CHECK USER INPUT
# ==========================================

def is_waiting_text(user_id):

    return user_id in user_waiting_text



# ==========================================
# GET TEXT
# ==========================================

def finish_text_input(user_id):

    user_waiting_text.discard(user_id)