# ==============================================================================
# LEVEL: Class Initializer
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Player:
    def __init__(self, name):
        self.name = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert Player('Alex').name == 'Alex', "Initializer check failed"
    print("🎉 LEVEL CLEARED! Mastered: Class Initializer")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
