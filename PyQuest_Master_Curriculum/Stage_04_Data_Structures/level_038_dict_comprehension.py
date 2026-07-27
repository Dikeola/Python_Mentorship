# ==============================================================================
# LEVEL: Dict Comprehension
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
squares = {x: x**2 for x in range(1, ___)}


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert squares == {1: 1, 2: 4, 3: 9}, "squares check failed"
    print("🎉 LEVEL CLEARED! Mastered: Dict Comprehension")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
