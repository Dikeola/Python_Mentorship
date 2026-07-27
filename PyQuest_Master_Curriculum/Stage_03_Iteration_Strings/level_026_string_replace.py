# ==============================================================================
# LEVEL: String Replacement
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
phrase = "I like Java"
updated = phrase.replace("Java", ___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert updated == 'I like Python', "updated must be 'I like Python'"
    print("🎉 LEVEL CLEARED! Mastered: String Replacement")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
