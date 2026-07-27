# ==============================================================================
# LEVEL: Reading Files with Context Manager
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
# Fill in the mode argument to open file for reading
file_content = ""
# with open("sample.txt", ___) as f:
#     file_content = f.read()
mode = "r" 


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert mode == 'r', "mode must equal 'r'"
    print("🎉 LEVEL CLEARED! Mastered: Reading Files with Context Manager")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
