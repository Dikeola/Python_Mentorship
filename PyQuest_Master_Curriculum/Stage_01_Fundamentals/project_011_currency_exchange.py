# ==============================================================================
# 🚀 PROJECT: Currency Exchange Calculator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def convert_currency(amount: float, exchange_rate: float) -> float:
    # Return amount * rate rounded to 2 decimal places
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert convert_currency(100.0, 1.25) == 125.0, "Test Failed"
print("🏆 PROJECT 011 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
