# ==============================================================================
# LEVEL: Loop Break
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
num = 0
while True:
    num += 1
    if num == 5:
        ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert num == 5, "num must equal 5"
    print("🎉 LEVEL CLEARED! Mastered: Loop Break")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
