# ==============================================================================
# 🚀 PROJECT: Mad Libs Generator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def create_mad_lib(noun: str, verb: str, adj: str) -> str:
    # Return formatted string: "The [adj] [noun] loved to [verb]."
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert create_mad_lib("cat", "sleep", "lazy") == "The lazy cat loved to sleep.", "Test 1 Failed"
assert create_mad_lib("robot", "code", "fast") == "The fast robot loved to code.", "Test 2 Failed"
print("🏆 PROJECT 002 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
