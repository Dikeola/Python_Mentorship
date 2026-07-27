# ==============================================================================
# 🚀 PROJECT: Energy & Mass Converter
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def mass_to_energy(mass_kg: float) -> float:
    # E = m * c^2 (use speed of light c = 300_000_000 m/s)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert mass_to_energy(1) == 9e16, "Test Failed"
print("🏆 PROJECT 015 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
