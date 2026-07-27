# ==============================================================================
# 🚀 PROJECT: Queue Operations Simulator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def queue_op(queue: list, action: str, item=None) -> tuple:
    # action "push": append item, return (None, updated_queue)
    # action "pop": remove first item, return (popped_item, updated_queue)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
q = [1, 2]
item, updated = queue_op(q, "pop")
assert item == 1 and updated == [2], "Test 1 Failed"
print("🏆 PROJECT 058 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
