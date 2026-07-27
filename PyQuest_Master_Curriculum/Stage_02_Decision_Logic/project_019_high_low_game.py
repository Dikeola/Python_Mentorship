# ==============================================================================
# 🚀 PROJECT: High-Low Guess Feedback
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def check_guess(secret: int, guess: int) -> str:
    # Return "Too High", "Too Low", or "Correct!"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert check_guess(50, 70) == "Too High", "Test 1 Failed"
assert check_guess(50, 20) == "Too Low", "Test 2 Failed"
assert check_guess(50, 50) == "Correct!", "Test 3 Failed"
print("🏆 PROJECT 019 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
