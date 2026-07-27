# ==============================================================================
# 🚀 PROJECT: Bill Splitter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def split_bill(total_amount: float, people: int, tip_pct: float) -> float:
    # Return cost per person rounded to 2 decimal places
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert split_bill(100.0, 4, 20.0) == 30.0, "Test 1 Failed"
assert split_bill(150.0, 3, 10.0) == 55.0, "Test 2 Failed"
print("🏆 PROJECT 009 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
