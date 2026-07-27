# ==============================================================================
# 🚀 PROJECT: Composable ETL Data Pipeline
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Pipeline:
    # Implement add_step(func) and process(data) passing data through steps sequentially
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
p = Pipeline()
p.add_step(lambda x: [i * 2 for i in x])
p.add_step(lambda x: [i for i in x if i > 5])

assert p.process([1, 2, 3, 4]) == [6, 8], "Test 1 Failed"
print("🏆 PROJECT 100 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
