# ==============================================================================
# LEVEL: Property Getters
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @property
    def area(self):
        return self.w * self.___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert Rectangle(4, 5).area == 20, "Property check failed"
    print("🎉 LEVEL CLEARED! Mastered: Property Getters")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
