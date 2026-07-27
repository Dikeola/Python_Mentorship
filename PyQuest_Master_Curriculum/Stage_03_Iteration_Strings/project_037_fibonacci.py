# ==============================================================================
# 🚀 PROJECT: Fibonacci Sequence Engine
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def fibonacci(n: int) -> list:
    # Return list of first n Fibonacci numbers (starting at 0, 1)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert fibonacci(5) == [0, 1, 1, 2, 3], "Test 1 Failed"
assert fibonacci(1) == [0], "Test 2 Failed"
print("🏆 PROJECT 037 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
