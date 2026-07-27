# ==============================================================================
# 🚀 PROJECT: Shipping Tier Calculator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def calculate_shipping(weight_kg: float, is_int: bool) -> float:
    # Base rate: domestic $5.0, international $15.0
    # Add $2.0 per kg for weight over 5kg
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert calculate_shipping(3, False) == 5.0, "Test 1 Failed"
assert calculate_shipping(7, False) == 9.0, "Test 2 Failed"
assert calculate_shipping(7, True) == 19.0, "Test 3 Failed"
print("🏆 PROJECT 028 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
