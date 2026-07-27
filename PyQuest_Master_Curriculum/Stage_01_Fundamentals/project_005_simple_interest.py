# ==============================================================================
# 🚀 PROJECT: Simple Interest Estimator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def calculate_interest(principal: float, rate_pct: float, time_years: float) -> float:
    # Formula: (Principal * Rate * Time) / 100
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert calculate_interest(1000, 5, 2) == 100.0, "Test 1 Failed"
assert calculate_interest(500, 10, 3) == 150.0, "Test 2 Failed"
print("🏆 PROJECT 005 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
