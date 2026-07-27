# ==============================================================================
# 🚀 PROJECT: Application Workflow State Machine
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class StateMachine:
    # Implement __init__(initial_state, transitions_dict)
    # transitions_dict format: {"IDLE": ["PROCESSING"], "PROCESSING": ["COMPLETED", "FAILED"]}
    # Implement transition_to(new_state) -> bool (returns True if valid transition, False otherwise)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
transitions = {
    "IDLE": ["PROCESSING"],
    "PROCESSING": ["COMPLETED", "FAILED"]
}

sm = StateMachine("IDLE", transitions)
assert sm.transition_to("COMPLETED") is False, "Test 1 Failed (Invalid direct jump)"
assert sm.transition_to("PROCESSING") is True, "Test 2 Failed"
assert sm.state == "PROCESSING", "Test 3 Failed"
print("🏆 PROJECT 105 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
