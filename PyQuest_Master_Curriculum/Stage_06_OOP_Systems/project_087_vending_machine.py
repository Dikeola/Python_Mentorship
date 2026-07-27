# ==============================================================================
# 🚀 PROJECT: Vending Machine State Machine
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class VendingMachine:
    # Implement insert_coin(amount: float), select_item(cost: float) -> tuple (success: bool, change: float)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
vm = VendingMachine()
vm.insert_coin(2.0)
success, change = vm.select_item(1.25)
assert success is True and change == 0.75, "Test 1 Failed"
print("🏆 PROJECT 087 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
