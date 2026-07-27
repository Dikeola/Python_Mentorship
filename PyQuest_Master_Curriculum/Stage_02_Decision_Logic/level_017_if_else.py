# ==============================================================================
# LEVEL: IF-ELSE Branching
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
is_logged_in = False
if is_logged_in:
    msg = "Welcome back"
else:
    msg = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert msg == 'Please log in', "msg must be 'Please log in'"
    print("🎉 LEVEL CLEARED! Mastered: IF-ELSE Branching")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
