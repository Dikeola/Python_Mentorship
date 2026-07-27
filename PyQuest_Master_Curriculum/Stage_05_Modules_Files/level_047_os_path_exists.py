# ==============================================================================
# LEVEL: Checking Path Existence
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
import os
# Check if current directory '.' exists
exists = os.path.exists(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert exists is True, "exists must be True"
    print("🎉 LEVEL CLEARED! Mastered: Checking Path Existence")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
