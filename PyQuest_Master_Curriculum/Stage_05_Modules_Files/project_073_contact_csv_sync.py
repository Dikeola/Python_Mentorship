# ==============================================================================
# 🚀 PROJECT: Contact Dict to CSV Generator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def contacts_to_csv(contacts: list) -> str:
    # contacts format: [{"name": "Alice", "phone": "123"}]
    # Return formatted CSV string with header "name,phone"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
c = [{"name": "Alice", "phone": "123"}]
assert contacts_to_csv(c) == "name,phone\nAlice,123", "Test 1 Failed"
print("🏆 PROJECT 073 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
