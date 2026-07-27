# ==============================================================================
# 🚀 PROJECT: BMI Calculator
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    # Formula: weight / (height ** 2), rounded to 2 decimal places
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert calculate_bmi(70, 1.75) == 22.86, "Test 1 Failed"
assert calculate_bmi(85, 1.80) == 26.23, "Test 2 Failed"
print("🏆 PROJECT 006 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
