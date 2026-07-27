# ==============================================================================
# 🚀 PROJECT: Inventory Quantity Manager
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def update_stock(inventory: dict, item: str, qty_change: int) -> dict:
    # Update inventory item count. If item missing, default starting stock is 0
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
inv = {"apple": 10}
res = update_stock(inv, "apple", -3)
assert res["apple"] == 7, "Test 1 Failed"
print("🏆 PROJECT 050 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
