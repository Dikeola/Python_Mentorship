# ==============================================================================
# LEVEL: Type Hint Annotations
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Complete the type annotation for a function returning an integer
def add(a: int, b: int) -> ___:
    return a + b


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert add.__annotations__.get('return') == int, "Return type annotation must be int"
    print("🎉 LEVEL CLEARED! Mastered: Type Hint Annotations")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
