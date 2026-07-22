"""
Khmer AI Studio
Navigation Controller
Version 5.5
Navigation History System
"""


# ==========================================
# NAVIGATION HISTORY
# ==========================================

class NavigationController:


    def __init__(self):

        self.stack = []



    # ======================================
    # GO TO NEW PAGE
    # ======================================

    def push(self, page):

        self.stack.append(page)



    # ======================================
    # GO BACK
    # ======================================

    def pop(self):

        if len(self.stack) > 1:

            self.stack.pop()

            return self.stack[-1]


        return "home"



    # ======================================
    # CURRENT PAGE
    # ======================================

    def current(self):

        if self.stack:

            return self.stack[-1]


        return "home"



    # ======================================
    # RESET
    # ======================================

    def reset(self):

        self.stack = ["home"]



    # ======================================
    # DEBUG
    # ======================================

    def show_history(self):

        return self.stack



# ==========================================
# GLOBAL INSTANCE
# ==========================================

navigation = NavigationController()