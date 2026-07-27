# ==============================================================================
# 🚀 PROJECT: Vowel Counter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def count_vowels(text: str) -> int:
    # Count total 'a', 'e', 'i', 'o', 'u' (case-insensitive)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert count_vowels("Hello World") == 3, "Test 1 Failed"
assert count_vowels("PyThOn") == 1, "Test 2 Failed"
print("🏆 PROJECT 034 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
