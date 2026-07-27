# ==============================================================================
# 🚀 PROJECT: Prime Number Checker
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def is_prime(n: int) -> bool:
    # Return True if n is prime (> 1), else False
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert is_prime(7) is True, "Test 1 Failed"
assert is_prime(4) is False, "Test 2 Failed"
assert is_prime(1) is False, "Test 3 Failed"
print("🏆 PROJECT 036 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
