# ==============================================================================
# LEVEL: Dictionary Safe .get()
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
inventory = {"apples": 5}
oranges = inventory.get("oranges", ___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert oranges == 0, "oranges must default to 0"
    print("🎉 LEVEL CLEARED! Mastered: Dictionary Safe .get()")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
