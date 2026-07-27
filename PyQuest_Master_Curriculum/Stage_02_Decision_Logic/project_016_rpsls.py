# ==============================================================================
# 🚀 PROJECT: Rock-Paper-Scissors-Spock
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def rpsls_winner(player: str, opponent: str) -> str:
    # Return "Player", "Opponent", or "Tie"
    # Rock beats Scissors; Paper beats Rock; Scissors beats Paper
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert rpsls_winner("Rock", "Scissors") == "Player", "Test 1 Failed"
assert rpsls_winner("Paper", "Rock") == "Player", "Test 2 Failed"
assert rpsls_winner("Rock", "Rock") == "Tie", "Test 3 Failed"
print("🏆 PROJECT 016 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
