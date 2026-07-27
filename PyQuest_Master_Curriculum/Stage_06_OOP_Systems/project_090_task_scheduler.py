# ==============================================================================
# 🚀 PROJECT: Priority Task Queue Scheduler
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class TaskScheduler:
    # Implement add_task(name, priority: int), run_next() -> str (task with highest priority number)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
ts = TaskScheduler()
ts.add_task("Low priority", 1)
ts.add_task("High priority", 10)
assert ts.run_next() == "High priority", "Test 1 Failed"
print("🏆 PROJECT 090 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
