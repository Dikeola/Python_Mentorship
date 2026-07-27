# ==============================================================================
# 🚀 PROJECT: Character Save State Encoder
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def serialize_character(name: str, level: int, hp: int) -> str:
    # Return formatted save string: "NAME|LEVEL|HP"
    pass

def deserialize_character(save_str: str) -> dict:
    # Parse "NAME|LEVEL|HP" back to dict {"name": str, "level": int, "hp": int}
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
s = serialize_character("Hero", 10, 100)
assert s == "Hero|10|100", "Test 1 Failed"
assert deserialize_character(s) == {"name": "Hero", "level": 10, "hp": 100}, "Test 2 Failed"
print("🏆 PROJECT 066 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
