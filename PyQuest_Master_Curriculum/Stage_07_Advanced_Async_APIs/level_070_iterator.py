# ==============================================================================
# LEVEL: Custom Iterator Methods
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class NumberSeries:
    def __init__(self, limit):
        self.limit = limit
        self.curr = 0
    def ___iter___(self):
        return self


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert hasattr(NumberSeries(5), '__iter__'), "__iter__ method check failed"
    print("🎉 LEVEL CLEARED! Mastered: Custom Iterator Methods")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
