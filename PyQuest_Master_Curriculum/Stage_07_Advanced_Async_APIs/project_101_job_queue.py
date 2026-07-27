# ==============================================================================
# 🚀 PROJECT: Prioritized Task Queue Engine
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class PriorityJobQueue:
    # Implement enqueue(job_name, priority: int) and dequeue() -> str
    # Dequeue retrieves job with HIGHEST priority (integer value)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
q = PriorityJobQueue()
q.enqueue("Task low", 1)
q.enqueue("Task critical", 10)
q.enqueue("Task medium", 5)

assert q.dequeue() == "Task critical", "Test 1 Failed"
assert q.dequeue() == "Task medium", "Test 2 Failed"
assert q.dequeue() == "Task low", "Test 3 Failed"
print("🏆 PROJECT 101 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
