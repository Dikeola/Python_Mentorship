# ==============================================================================
# 🚀 PROJECT: Temperature Converter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def celsius_to_fahrenheit(c: float) -> float:
    # Formula: (C * 9/5) + 32
    pass

def fahrenheit_to_celsius(f: float) -> float:
    # Formula: (F - 32) * 5/9
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert celsius_to_fahrenheit(0) == 32.0, "C to F Failed"
assert celsius_to_fahrenheit(100) == 212.0, "C to F Failed"
assert fahrenheit_to_celsius(32) == 0.0, "F to C Failed"
assert fahrenheit_to_celsius(212) == 100.0, "F to C Failed"
print("🏆 PROJECT 003 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
