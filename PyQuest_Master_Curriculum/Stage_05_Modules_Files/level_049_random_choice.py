# ==============================================================================
# LEVEL: Random Choices
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
import random
options = ["rock", "paper", "scissors"]
# Fill in the random function to pick one element
picked = random.choice(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert picked in ['rock', 'paper', 'scissors'], "picked must be a valid option"
    print("🎉 LEVEL CLEARED! Mastered: Random Choices")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
