# ==============================================================================
# 🚀 PROJECT: Age in Days Calculator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def age_in_days(years: int) -> int:
    # Assume 365 days per year (ignore leap years)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert age_in_days(25) == 9125, "Test Failed"
print("🏆 PROJECT 007 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
