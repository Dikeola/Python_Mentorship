# ==============================================================================
# 🚀 PROJECT: Single Character Caesar Shift
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def shift_char(char: str, shift: int) -> str:
    # Shift lowercase alphabetic char by shift amount (wrap around 'a'-'z')
    # If not lowercase alpha, return unchanged
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert shift_char('a', 2) == 'c', "Test 1 Failed"
assert shift_char('z', 1) == 'a', "Test 2 Failed"
assert shift_char('!', 5) == '!', "Test 3 Failed"
print("🏆 PROJECT 021 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
