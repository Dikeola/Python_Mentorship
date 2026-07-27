# ==============================================================================
# 🚀 PROJECT: In-Memory Data Table
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Table:
    # Implement insert(row_dict), select_where(key, value) -> list of dicts
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
t = Table()
t.insert({"id": 1, "role": "admin"})
t.insert({"id": 2, "role": "user"})
assert t.select_where("role", "admin") == [{"id": 1, "role": "admin"}], "Test 1 Failed"
print("🏆 PROJECT 084 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
