# ==============================================================================
# LEVEL: ELIF Conditional Chains
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = ___
else:
    grade = "C" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert grade == 'B', "grade must be 'B'"
    print("🎉 LEVEL CLEARED! Mastered: ELIF Conditional Chains")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
