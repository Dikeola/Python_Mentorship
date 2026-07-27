# ==============================================================================
# 🚀 PROJECT: Morse Code Translator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

MORSE_MAP = {'A': '.-', 'B': '-...', 'C': '-.-.', 'S': '...', 'O': '---'}

def to_morse(text: str) -> str:
    # Translate uppercase letters to morse separated by single space
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert to_morse("SOS") == "... --- ...", "Test 1 Failed"
print("🏆 PROJECT 033 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
