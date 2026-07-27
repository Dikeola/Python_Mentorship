# ==============================================================================
# LEVEL: Set Intersection
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
set_a = {1, 2, 3}
set_b = {2, 3, 4}
common = set_a.___ (set_b)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert common == {2, 3}, "common must equal {2, 3}"
    print("🎉 LEVEL CLEARED! Mastered: Set Intersection")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
