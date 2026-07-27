# ==============================================================================
# 🚀 PROJECT: File Archive Filter
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def filter_for_backup(file_list: list, extension: str) -> list:
    # Return list of files that end with specified extension
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
files = ["notes.txt", "script.py", "data.txt"]
assert filter_for_backup(files, ".txt") == ["notes.txt", "data.txt"], "Test 1 Failed"
print("🏆 PROJECT 072 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
