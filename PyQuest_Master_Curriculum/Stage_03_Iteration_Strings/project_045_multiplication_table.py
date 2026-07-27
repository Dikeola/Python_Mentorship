# ==============================================================================
# 🚀 PROJECT: Multiplication Grid Generator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def multiplication_table(size: int) -> list:
    # Return size x size nested list grid
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]], "Test 1 Failed"
print("🏆 PROJECT 045 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
