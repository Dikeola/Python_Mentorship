# ==============================================================================
# LEVEL: Writing Files
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Fill in the mode argument to overwrite a file
mode = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert mode == 'w', "mode must equal 'w'"
    print("🎉 LEVEL CLEARED! Mastered: Writing Files")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
