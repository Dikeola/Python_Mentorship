# ==============================================================================
# 🚀 PROJECT: Election Winner Counter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def tally_votes(votes: list) -> str:
    # Return winning candidate name (most frequent string)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert tally_votes(["Alice", "Bob", "Alice"]) == "Alice", "Test 1 Failed"
print("🏆 PROJECT 055 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
