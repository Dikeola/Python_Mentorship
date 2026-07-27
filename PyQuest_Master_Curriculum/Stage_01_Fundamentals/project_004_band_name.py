# ==============================================================================
# 🚀 PROJECT: Band Name Generator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def generate_band_name(city: str, pet: str) -> str:
    # Return "The " + City + " " + Pet (capitalized correctly)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert generate_band_name("Austin", "Viper") == "The Austin Viper", "Test Failed"
print("🏆 PROJECT 004 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
