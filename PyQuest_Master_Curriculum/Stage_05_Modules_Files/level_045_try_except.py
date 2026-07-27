# ==============================================================================
# LEVEL: Exception Handling
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
try:
    result = 10 / 0
except ___:
    result = 0


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert result == 0, "result must equal 0"
    print("🎉 LEVEL CLEARED! Mastered: Exception Handling")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
