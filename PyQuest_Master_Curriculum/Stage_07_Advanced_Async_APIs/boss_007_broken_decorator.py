# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Returning Function Results in Decorator
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix this decorator so it returns the actual function execution result instead of None
def audit_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        # Fix line below so result is captured and returned
        func(*args, **kwargs)
    return wrapper

@audit_logger
def compute_sum(a, b):
    return a + b


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert compute_sum(10, 20) == 30, "Decorator function result check failed"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
