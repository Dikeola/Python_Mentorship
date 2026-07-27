# ==============================================================================
# LEVEL: Class Inheritance
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Animal:
    def speak(self): return "Sound"

class Dog(___):
    pass


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert issubclass(Dog, Animal), "Dog must inherit from Animal"
    print("🎉 LEVEL CLEARED! Mastered: Class Inheritance")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
