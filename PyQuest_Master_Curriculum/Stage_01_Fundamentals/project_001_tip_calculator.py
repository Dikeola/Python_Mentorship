# ==============================================================================
# 🚀 PROJECT: Tip & Tax Calculator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def calculate_total(bill: float, tip_pct: float, tax_pct: float) -> float:
    # Return (bill + tip + tax) rounded to 2 decimal places
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert calculate_total(100.0, 15, 10) == 125.0, "Test 1 Failed: 100 + 15% tip + 10% tax = 125.0"
assert calculate_total(50.0, 20, 8) == 64.0, "Test 2 Failed: 50 + 20% tip + 8% tax = 64.0"
print("🏆 PROJECT 001 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
