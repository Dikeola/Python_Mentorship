# ==============================================================================
# 🚀 PROJECT: Chess Rook Movement Rules
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Rook:
    def is_valid_move(self, start: tuple, end: tuple) -> bool:
        # Valid if moving along same row (start[0]==end[0]) OR same col (start[1]==end[1]), and start != end
        pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
r = Rook()
assert r.is_valid_move((0,0), (0,5)) is True, "Test 1 Failed"
assert r.is_valid_move((0,0), (2,3)) is False, "Test 2 Failed"
print("🏆 PROJECT 085 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
