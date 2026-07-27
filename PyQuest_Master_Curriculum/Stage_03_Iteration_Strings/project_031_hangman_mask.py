# ==============================================================================
# 🚀 PROJECT: Hangman Word Masking
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def mask_word(secret_word: str, guessed_letters: list) -> str:
    # Reveal guessed letters, replace un-guessed lowercase alpha chars with '_'
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert mask_word("python", ['p', 'o']) == "p_t_o_", "Test 1 Failed"
assert mask_word("code", ['c', 'o', 'd', 'e']) == "code", "Test 2 Failed"
print("🏆 PROJECT 031 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
