# ==============================================================================
# 🚀 PROJECT: Single/Double Digit Converter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def number_to_word(n: int) -> str:
    # Convert 1-10 into capital word e.g. 1 -> "One", 5 -> "Five"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert number_to_word(1) == "One", "Test 1 Failed"
assert number_to_word(10) == "Ten", "Test 2 Failed"
print("🏆 PROJECT 044 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
