# ==============================================================================
# LEVEL: Loop Continue
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
evens_sum = 0
for i in range(1, 6):
    if i % 2 != 0:
        ___
    evens_sum += i


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert evens_sum == 6, "evens_sum must equal 6"
    print("🎉 LEVEL CLEARED! Mastered: Loop Continue")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
