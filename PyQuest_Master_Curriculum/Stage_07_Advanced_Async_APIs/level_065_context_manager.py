# ==============================================================================
# LEVEL: Custom Context Manager
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class ManagedResource:
    def __enter__(self):
        return "resource"
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Context manager uses the ___ keyword
kw = "with" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert kw == 'with', "Keyword must be 'with'"
    print("🎉 LEVEL CLEARED! Mastered: Custom Context Manager")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
