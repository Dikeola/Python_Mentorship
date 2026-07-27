# ==============================================================================
# 🚀 PROJECT: Priority Todo List Manager
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def add_task(todo_list: list, task_name: str, priority: int) -> list:
    # Append item dict {"task": task_name, "priority": priority}
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
l = []
res = add_task(l, "Buy Milk", 1)
assert res == [{"task": "Buy Milk", "priority": 1}], "Test 1 Failed"
print("🏆 PROJECT 046 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
