# ==============================================================================
# LEVEL: Generator Functions with Yield
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Fill in the yield keyword to make this a generator
def count_up(n):
    for i in range(1, n + 1):
        ___ i


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert list(count_up(3)) == [1, 2, 3], "Generator yield check failed"
    print("🎉 LEVEL CLEARED! Mastered: Generator Functions with Yield")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
