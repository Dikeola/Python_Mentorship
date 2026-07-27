# ==============================================================================
# 🚀 PROJECT: JSON Config Manipulator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

import json

def update_config(json_str: str, key: str, value) -> str:
    # Parse json_str, update key-value pair, return updated formatted JSON string
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
raw = '{"theme": "light", "volume": 50}'
res = update_config(raw, "theme", "dark")
assert json.loads(res)["theme"] == "dark", "Test 1 Failed"
print("🏆 PROJECT 062 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
