# ==============================================================================
# 🚀 PROJECT: Word Counter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def count_words(text: str) -> int:
    # Return number of words separated by whitespace
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert count_words("Python is awesome!") == 3, "Test 1 Failed"
assert count_words("  Hello   World ") == 2, "Test 2 Failed"
print("🏆 PROJECT 038 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
