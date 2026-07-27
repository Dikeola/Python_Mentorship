# ==============================================================================
# 🚀 PROJECT: Expense Categorizer
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def categorize_expenses(transactions: list) -> dict:
    # transactions format: [("Food", 10), ("Food", 15), ("Gas", 30)]
    # Sum totals per category dict
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
data = [("Food", 10), ("Food", 15), ("Gas", 30)]
assert categorize_expenses(data) == {"Food": 25, "Gas": 30}, "Test 1 Failed"
print("🏆 PROJECT 054 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
