# ==============================================================================
# LEVEL: Async Coroutines
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
import asyncio

# Fill in the keyword to define an asynchronous function
___ def fetch_data():
    return "data" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert asyncio.iscoroutinefunction(fetch_data), "fetch_data must be an async coroutine"
    print("🎉 LEVEL CLEARED! Mastered: Async Coroutines")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
