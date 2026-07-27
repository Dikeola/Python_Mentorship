# ==============================================================================
# LEVEL: Function Decorators
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Fill in the decorator syntax keyword
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# @___
# def greet(): return "Hello"
decorator_symbol = "@" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert decorator_symbol == '@', "Decorator symbol must be '@'"
    print("🎉 LEVEL CLEARED! Mastered: Function Decorators")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
