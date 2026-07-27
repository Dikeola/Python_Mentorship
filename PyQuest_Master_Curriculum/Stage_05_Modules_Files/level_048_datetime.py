# ==============================================================================
# LEVEL: Working with Datetime
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
from datetime import datetime
now = datetime.now()
year = now.___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert isinstance(year, int), "year must be an integer"
    print("🎉 LEVEL CLEARED! Mastered: Working with Datetime")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
