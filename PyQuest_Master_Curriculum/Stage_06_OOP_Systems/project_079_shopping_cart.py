# ==============================================================================
# 🚀 PROJECT: E-Commerce Shopping Cart
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class ShoppingCart:
    # Implement add_item(name, price), apply_discount(pct), calculate_total() -> float
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
cart = ShoppingCart()
cart.add_item("Shirt", 20.0)
cart.add_item("Pants", 30.0)
cart.apply_discount(10) # 10% off total
assert cart.calculate_total() == 45.0, "Test 1 Failed"
print("🏆 PROJECT 079 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
