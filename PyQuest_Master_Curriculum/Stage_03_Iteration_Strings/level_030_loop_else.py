# ==============================================================================
# LEVEL: Loop Else Clause
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
found = False
for x in [1, 2, 3]:
    if x == 99:
        found = True
        break
else:
    msg = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert msg == 'Not Found', "msg must equal 'Not Found'"
    print("🎉 LEVEL CLEARED! Mastered: Loop Else Clause")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
