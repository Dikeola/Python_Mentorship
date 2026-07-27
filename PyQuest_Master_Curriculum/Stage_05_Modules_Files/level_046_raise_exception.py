# ==============================================================================
# LEVEL: Raising Exceptions
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
def check_age(age):
    if age < 0:
        raise ___("Age cannot be negative")
    return age


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert True, "Validation check"
    print("🎉 LEVEL CLEARED! Mastered: Raising Exceptions")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
