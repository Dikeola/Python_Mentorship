# ==============================================================================
# 🚀 PROJECT: Scrabble Word Scorer
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

SCORES = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1}

def scrabble_score(word: str) -> int:
    # Calculate score using SCORES dict (case-insensitive)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert scrabble_score("CAB") == 7, "Test 1 Failed"
print("🏆 PROJECT 051 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
