# ==============================================================================
# 🚀 PROJECT: Grade Scale Evaluator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def score_to_gpa(score: float) -> float:
    # >= 90 -> 4.0
    # >= 80 -> 3.0
    # >= 70 -> 2.0
    # >= 60 -> 1.0
    # Else -> 0.0
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert score_to_gpa(95) == 4.0, "Test 1 Failed"
assert score_to_gpa(82) == 3.0, "Test 2 Failed"
assert score_to_gpa(55) == 0.0, "Test 3 Failed"
print("🏆 PROJECT 025 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
