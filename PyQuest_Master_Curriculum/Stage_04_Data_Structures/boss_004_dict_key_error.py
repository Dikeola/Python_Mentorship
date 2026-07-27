# ==============================================================================
# ⚔️ BOSS FIGHT: Fix KeyError Exception
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix code to safely retrieve 'role' without crashing with KeyError
user_profile = {"username": "dev_hero"}
# Change indexing to safe .get() method
user_role = user_profile["role"]


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert user_role == 'Guest', "user_role must fall back to 'Guest'"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
