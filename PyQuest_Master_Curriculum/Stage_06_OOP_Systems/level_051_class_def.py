# ==============================================================================
# LEVEL: Defining a Class
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Hero:
    pass

# Instantiate Hero object
player = ___()


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert isinstance(player, Hero), "player must be an instance of Hero"
    print("🎉 LEVEL CLEARED! Mastered: Defining a Class")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
