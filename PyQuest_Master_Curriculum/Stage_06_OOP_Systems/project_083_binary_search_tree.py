# ==============================================================================
# 🚀 PROJECT: Binary Search Tree Node Lookup
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class BSTNode:
    # Implement __init__(val), insert(val), contains(val) -> bool
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
root = BSTNode(10)
root.insert(5)
root.insert(15)
assert root.contains(5) is True, "Test 1 Failed"
assert root.contains(99) is False, "Test 2 Failed"
print("🏆 PROJECT 083 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
