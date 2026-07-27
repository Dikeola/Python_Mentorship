# ==============================================================================
# LEVEL: Parsing CSV Lines
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
raw_csv = "name,score\nAlice,100\nBob,90"
lines = raw_csv.splitlines()
header = lines[0].split(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert header == ['name', 'score'], "header must be ['name', 'score']"
    print("🎉 LEVEL CLEARED! Mastered: Parsing CSV Lines")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
