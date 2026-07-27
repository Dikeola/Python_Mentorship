# ==============================================================================
# LEVEL: Super Class Call
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        ___.__init__(name)
        self.age = age


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert Child('Sam', 10).name == 'Sam', "super() call check failed"
    print("🎉 LEVEL CLEARED! Mastered: Super Class Call")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
