# ==============================================================================
# 🚀 PROJECT: Traffic Light State Engine
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def next_light(current: str) -> str:
    # "Red" -> "Green"
    # "Green" -> "Yellow"
    # "Yellow" -> "Red"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert next_light("Red") == "Green", "Test 1 Failed"
assert next_light("Green") == "Yellow", "Test 2 Failed"
assert next_light("Yellow") == "Red", "Test 3 Failed"
print("🏆 PROJECT 026 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
