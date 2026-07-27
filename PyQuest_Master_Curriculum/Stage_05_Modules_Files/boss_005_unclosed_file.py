# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Unhandled File Exception & Closure
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix this code to use a context manager (with block) so files close properly
def read_log(filename):
    # Fix using with open(filename, 'r')
    f = open(filename, 'r')
    content = f.read()
    return content


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert True, "Context manager check"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
