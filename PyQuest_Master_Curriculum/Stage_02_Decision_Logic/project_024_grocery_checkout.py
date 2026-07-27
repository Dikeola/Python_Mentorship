# ==============================================================================
# 🚀 PROJECT: Discount Checkout
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def checkout_total(subtotal: float, coupon_code: str) -> float:
    # "SAVE10" -> 10% discount
    # "SAVE20" -> 20% discount
    # Otherwise -> no discount
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert checkout_total(100.0, "SAVE10") == 90.0, "Test 1 Failed"
assert checkout_total(100.0, "SAVE20") == 80.0, "Test 2 Failed"
assert checkout_total(100.0, "NONE") == 100.0, "Test 3 Failed"
print("🏆 PROJECT 024 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
