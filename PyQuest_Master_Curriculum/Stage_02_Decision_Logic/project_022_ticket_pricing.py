# ==============================================================================
# 🚀 PROJECT: Movie Ticket Pricing
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def get_ticket_price(age: int, is_matinee: bool) -> float:
    # Under 12 or over 65 -> $8.0 (Matinee) or $10.0 (Standard)
    # Others -> $10.0 (Matinee) or $15.0 (Standard)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert get_ticket_price(10, True) == 8.0, "Test 1 Failed"
assert get_ticket_price(25, False) == 15.0, "Test 2 Failed"
assert get_ticket_price(25, True) == 10.0, "Test 3 Failed"
print("🏆 PROJECT 022 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
