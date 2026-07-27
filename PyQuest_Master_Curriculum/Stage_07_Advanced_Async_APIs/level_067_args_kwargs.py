# ==============================================================================
# LEVEL: Variadic Arguments (*args, **kwargs)
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
def collect_all(*args, **kwargs):
    return len(args) + len(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert collect_all(1, 2, a=3) == 3, "*args and **kwargs check failed"
    print("🎉 LEVEL CLEARED! Mastered: Variadic Arguments (*args, **kwargs)")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
