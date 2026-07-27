# ==============================================================================
# 🚀 PROJECT: Triangle Inequality Checker
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def isValidTriangle(a: float, b: float, c: float) -> bool:
    # Valid if sum of any two sides is greater than the third
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert isValidTriangle(3, 4, 5) is True, "Test 1 Failed"
assert isValidTriangle(1, 2, 3) is False, "Test 2 Failed"
print("🏆 PROJECT 030 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
