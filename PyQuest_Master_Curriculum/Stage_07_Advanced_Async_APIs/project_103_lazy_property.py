# ==============================================================================
# 🚀 PROJECT: Lazy Property Evaluator
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class lazy_property:
    # Descriptor decorator that computes property value once and caches it on the instance attribute dict
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
class DataModel:
    def __init__(self):
        self.computations = 0

    @lazy_property
    def heavy_value(self):
        self.computations += 1
        return 42

m = DataModel()
assert m.computations == 0, "Test 1 Failed"
assert m.heavy_value == 42, "Test 2 Failed"
assert m.heavy_value == 42, "Test 3 Failed"
assert m.computations == 1, "Test 4 Failed (Value should be lazily computed once)"
print("🏆 PROJECT 103 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
