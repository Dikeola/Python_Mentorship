# ==============================================================================
# LEVEL: Custom Exception Classes
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class ApplicationError(___):
    pass


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert issubclass(ApplicationError, Exception), "ApplicationError must inherit from Exception"
    print("🎉 LEVEL CLEARED! Mastered: Custom Exception Classes")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
