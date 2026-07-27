# ==============================================================================
# LEVEL: Lambda Anonymous Functions
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Fill in the keyword to create an anonymous inline function
square = ___ x: x ** 2


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert square(4) == 16, "Lambda calculation failed"
    print("🎉 LEVEL CLEARED! Mastered: Lambda Anonymous Functions")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
