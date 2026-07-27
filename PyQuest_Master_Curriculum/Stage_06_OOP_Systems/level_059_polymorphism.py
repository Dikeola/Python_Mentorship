# ==============================================================================
# LEVEL: Polymorphic Methods
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Cat:
    def talk(self): return "Meow"
class Duck:
    def talk(self): return "Quack"

def make_it_talk(obj):
    return obj.___()


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert make_it_talk(Cat()) == 'Meow', "Polymorphism check failed"
    print("🎉 LEVEL CLEARED! Mastered: Polymorphic Methods")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
