# ==============================================================================
# LEVEL: __str__ Dunder Method
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Item: {self.___}" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert str(Item('Sword')) == 'Item: Sword', "__str__ check failed"
    print("🎉 LEVEL CLEARED! Mastered: __str__ Dunder Method")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
