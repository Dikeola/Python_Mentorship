# ==============================================================================
# 🚀 PROJECT: Hotel Reservation System
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Hotel:
    # Implement __init__(num_rooms), book_room() -> int (room_number or -1 if full)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
h = Hotel(2)
r1 = h.book_room()
r2 = h.book_room()
r3 = h.book_room()
assert r1 == 1 and r2 == 2 and r3 == -1, "Test 1 Failed"
print("🏆 PROJECT 080 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
