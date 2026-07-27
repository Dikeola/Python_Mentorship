# ==============================================================================
# 🚀 PROJECT: Singly Linked List Implementation
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    # Implement append(val), to_list() -> list
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
ll = LinkedList()
ll.append(1)
ll.append(2)
assert ll.to_list() == [1, 2], "Test 1 Failed"
print("🏆 PROJECT 082 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
