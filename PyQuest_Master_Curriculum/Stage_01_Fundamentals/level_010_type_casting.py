# ==============================================================================
# LEVEL: Type Casting
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
raw = '50'
number = int(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert number == 50 and isinstance(number, int), "number must be integer 50"
    print("🎉 LEVEL CLEARED! Mastered: Type Casting")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
