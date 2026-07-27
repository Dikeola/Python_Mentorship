# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Unreachable Code
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix the logic order so score 95 returns "A" and score 75 returns "C"
score = 95
if score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"
else:
    grade = "F" 


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert grade == 'A', "grade must be 'A'"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
