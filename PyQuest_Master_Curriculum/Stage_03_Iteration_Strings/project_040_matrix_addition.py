# ==============================================================================
# 🚀 PROJECT: Matrix Addition Engine
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def add_matrices(mat_a: list, mat_b: list) -> list:
    # Return sum of two 2D matrices of equal dimensions
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
assert add_matrices(a, b) == [[6, 8], [10, 12]], "Test 1 Failed"
print("🏆 PROJECT 040 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
