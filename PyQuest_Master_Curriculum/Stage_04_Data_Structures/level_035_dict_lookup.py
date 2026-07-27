# ==============================================================================
# LEVEL: Dictionary Value Lookup
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
user = {"name": "Alex", "age": 25}
user_name = user[___]


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert user_name == 'Alex', "user_name must be 'Alex'"
    print("🎉 LEVEL CLEARED! Mastered: Dictionary Value Lookup")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
