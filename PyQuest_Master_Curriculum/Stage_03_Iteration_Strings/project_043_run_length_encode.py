# ==============================================================================
# 🚀 PROJECT: Run-Length Text Encoder
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def rle_encode(text: str) -> str:
    # E.g. "AAABBC" -> "3A2B1C"
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert rle_encode("AAABBC") == "3A2B1C", "Test 1 Failed"
assert rle_encode("X") == "1X", "Test 2 Failed"
print("🏆 PROJECT 043 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
