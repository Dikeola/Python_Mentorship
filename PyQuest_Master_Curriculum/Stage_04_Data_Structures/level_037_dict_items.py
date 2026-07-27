# ==============================================================================
# LEVEL: Dictionary .items() Loop
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
data = {"a": 1, "b": 2}
keys_str = ""
for k, v in data.___():
    keys_str += k


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert keys_str == 'ab', "keys_str must equal 'ab'"
    print("🎉 LEVEL CLEARED! Mastered: Dictionary .items() Loop")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
