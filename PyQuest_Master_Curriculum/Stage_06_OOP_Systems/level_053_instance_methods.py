# ==============================================================================
# LEVEL: Instance Methods
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Counter:
    def __init__(self):
        self.val = 0
    def increment(self):
        self.val += ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert c = Counter(); c.increment(); c.val == 1, "Method check failed"
    print("🎉 LEVEL CLEARED! Mastered: Instance Methods")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
