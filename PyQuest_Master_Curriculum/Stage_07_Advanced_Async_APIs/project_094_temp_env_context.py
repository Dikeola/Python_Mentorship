# ==============================================================================
# 🚀 PROJECT: Temporary Environment Variable Manager
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

import os

class TempEnv:
    # Context manager setting os.environ[key] = value, restoring original value or deleting upon exit
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
import os

os.environ["TEST_VAR"] = "ORIGINAL"
with TempEnv("TEST_VAR", "MODIFIED"):
    assert os.environ["TEST_VAR"] == "MODIFIED", "Test 1 Failed"
assert os.environ["TEST_VAR"] == "ORIGINAL", "Test 2 Failed"
print("🏆 PROJECT 094 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
