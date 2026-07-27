# ==============================================================================
# 🚀 PROJECT: Basic Roman Numeral Converter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def to_roman(num: int) -> str:
    # Convert integer (1 to 100) to Roman Numeral string
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert to_roman(4) == "IV", "Test 1 Failed"
assert to_roman(9) == "IX", "Test 2 Failed"
assert to_roman(58) == "LVIII", "Test 3 Failed"
print("🏆 PROJECT 035 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
