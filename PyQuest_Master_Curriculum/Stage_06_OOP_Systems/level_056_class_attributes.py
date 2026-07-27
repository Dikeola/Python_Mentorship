# ==============================================================================
# LEVEL: Class Attributes vs Instance Attributes
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Circle:
    pi = 3.14159
    def __init__(self, r):
        self.r = r

# Access class attribute pi from class
p = Circle.___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert p == 3.14159, "Class attribute check failed"
    print("🎉 LEVEL CLEARED! Mastered: Class Attributes vs Instance Attributes")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
