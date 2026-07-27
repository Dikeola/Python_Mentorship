# ==============================================================================
# LEVEL: Python Dataclasses
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
from dataclasses import dataclass

# Fill in the dataclass decorator
@___
class User:
    id: int
    name: str


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert User(1, 'Alice').name == 'Alice', "Dataclass check failed"
    print("🎉 LEVEL CLEARED! Mastered: Python Dataclasses")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
