# ==============================================================================
# 🚀 PROJECT: Expense Text Serializer
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def serialize_expenses(expenses: list) -> str:
    # expenses format: [("Food", 12.5), ("Gas", 30.0)]
    # Convert to multiline pipe-delimited string: "Food|12.5\nGas|30.0"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
exp = [("Food", 12.5), ("Gas", 30.0)]
assert serialize_expenses(exp) == "Food|12.5\nGas|30.0", "Test 1 Failed"
print("🏆 PROJECT 070 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
