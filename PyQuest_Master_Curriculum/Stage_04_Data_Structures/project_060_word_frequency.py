# ==============================================================================
# 🚀 PROJECT: Top Word Frequency Ranker
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def top_frequent(text: str, n: int) -> list:
    # Return list of top 'n' most frequent words (lowercase)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert top_frequent("the cat in the hat", 1) == ["the"], "Test 1 Failed"
print("🏆 PROJECT 060 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
