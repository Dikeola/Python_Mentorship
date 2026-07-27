# ==============================================================================
# LEVEL: Simple IF Statement
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
age = 20
status = "Minor"
if age >= 18:
    status = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert status == 'Adult', "status must be 'Adult'"
    print("🎉 LEVEL CLEARED! Mastered: Simple IF Statement")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
