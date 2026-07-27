# ==============================================================================
# 🚀 PROJECT: Password Evaluator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def evaluate_password(pwd: str) -> str:
    # Length < 6 -> "Weak"
    # Length >= 6 and contains at least 1 digit -> "Strong"
    # Otherwise -> "Moderate"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert evaluate_password("12345") == "Weak", "Test 1 Failed"
assert evaluate_password("secret") == "Moderate", "Test 2 Failed"
assert evaluate_password("secret1") == "Strong", "Test 3 Failed"
print("🏆 PROJECT 018 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
