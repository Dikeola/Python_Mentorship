# ==============================================================================
# 🚀 PROJECT: Nested List Flattening Iterator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class FlattenIterator:
    # Custom iterator taking a list of lists and iterating through all items flatly
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
items = [[1, 2], [3], [4, 5]]
assert list(FlattenIterator(items)) == [1, 2, 3, 4, 5], "Test 1 Failed"
print("🏆 PROJECT 098 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
