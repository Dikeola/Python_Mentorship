# ==============================================================================
# 🚀 PROJECT: Seat Reservation System
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def book_seat(chart: list, row: int, col: int) -> list:
    # Set seat from "O" to "X" if empty, return updated chart
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
chart = [["O", "O"]]
assert book_seat(chart, 0, 1) == [["O", "X"]], "Test 1 Failed"
print("🏆 PROJECT 059 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
