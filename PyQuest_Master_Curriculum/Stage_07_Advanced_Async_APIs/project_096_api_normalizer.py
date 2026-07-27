# ==============================================================================
# 🚀 PROJECT: Inconsistent API Payload Normalizer
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def normalize_user_payload(raw_payload: dict) -> dict:
    # Convert payloads with keys ("user_name" or "name") and ("mail" or "email")
    # into standard dict format: {"name": str, "email": str, "active": bool (default True)}
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
p1 = {"user_name": "Alice", "mail": "alice@test.com"}
p2 = {"name": "Bob", "email": "bob@test.com", "active": False}

assert normalize_user_payload(p1) == {"name": "Alice", "email": "alice@test.com", "active": True}, "Test 1 Failed"
assert normalize_user_payload(p2) == {"name": "Bob", "email": "bob@test.com", "active": False}, "Test 2 Failed"
print("🏆 PROJECT 096 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
