# ==============================================================================
# LEVEL: Nested Loops
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
stars = ""
for i in range(2):
    for j in range(2):
        stars += ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert stars == '****', "stars must equal '****'"
    print("🎉 LEVEL CLEARED! Mastered: Nested Loops")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
