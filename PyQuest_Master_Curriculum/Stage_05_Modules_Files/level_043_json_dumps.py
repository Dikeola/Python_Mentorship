# ==============================================================================
# LEVEL: JSON Serialization
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
import json
data = {"status": "ok", "code": 200}
json_string = json.dumps(___)


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert 'status' in json_string, "json_string must contain key 'status'"
    print("🎉 LEVEL CLEARED! Mastered: JSON Serialization")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
