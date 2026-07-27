# ==============================================================================
# 🚀 PROJECT: ATM Transaction Logic
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def atm_transaction(balance: float, action: str, amount: float) -> float:
    # action "deposit" -> balance + amount
    # action "withdraw" -> if amount <= balance balance - amount else balance
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert atm_transaction(100.0, "deposit", 50.0) == 150.0, "Test 1 Failed"
assert atm_transaction(100.0, "withdraw", 40.0) == 60.0, "Test 2 Failed"
assert atm_transaction(100.0, "withdraw", 150.0) == 100.0, "Test 3 Failed"
print("🏆 PROJECT 020 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
