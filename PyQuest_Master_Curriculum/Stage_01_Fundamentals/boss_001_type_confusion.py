# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Type Mismatches
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix the code so total equals 30 as an integer
val1 = "10"
val2 = 20
total = ___


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert total == 30, "total must equal 30 as an integer"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
