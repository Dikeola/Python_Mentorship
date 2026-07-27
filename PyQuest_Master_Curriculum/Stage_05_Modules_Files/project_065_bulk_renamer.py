# ==============================================================================
# 🚀 PROJECT: Batch File Name Formatter
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def format_filenames(filenames: list, prefix: str) -> list:
    # Format list of filenames to '[prefix]_[index].[ext]' preserving extension
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
files = ["doc1.pdf", "img.png"]
assert format_filenames(files, "vacation") == ["vacation_1.pdf", "vacation_2.png"], "Test 1 Failed"
print("🏆 PROJECT 065 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
