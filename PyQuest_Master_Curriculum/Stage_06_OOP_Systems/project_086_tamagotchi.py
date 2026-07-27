# ==============================================================================
# 🚀 PROJECT: Virtual Pet Simulator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Pet:
    # Implement __init__(name), feed(), play(), status() -> dict {"hunger": int, "happiness": int}
    # Initial: hunger 5, happiness 5. feed() -> hunger -2. play() -> happiness +2.
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
p = Pet("Fluffy")
p.feed()
p.play()
assert p.status() == {"hunger": 3, "happiness": 7}, "Test 1 Failed"
print("🏆 PROJECT 086 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
