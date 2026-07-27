# ==============================================================================
# 🚀 PROJECT: Nested Directory Size Calculator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def calculate_total_size(node: dict) -> int:
    # node can be integer (file size) or dict (folder containing nodes)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
folder = {"file1.txt": 100, "sub": {"file2.txt": 250}}
assert calculate_total_size(folder) == 350, "Test 1 Failed"
print("🏆 PROJECT 071 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
