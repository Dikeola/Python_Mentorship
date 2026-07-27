# ==============================================================================
# LEVEL: Logical AND
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
check = (5 > 2) and (10 < ___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert check is True, "check must be True"
    print("🎉 LEVEL CLEARED! Mastered: Logical AND")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
