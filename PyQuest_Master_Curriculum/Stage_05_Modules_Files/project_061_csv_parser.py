# ==============================================================================
# 🚀 PROJECT: CSV Text Data Parser
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def parse_csv_string(csv_data: str) -> list:
    # Convert comma-separated string into a list of dictionaries using first line as headers
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
data = "name,age\nAlice,30\nBob,25"
res = parse_csv_string(data)
assert res == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}], "Test 1 Failed"
print("🏆 PROJECT 061 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
