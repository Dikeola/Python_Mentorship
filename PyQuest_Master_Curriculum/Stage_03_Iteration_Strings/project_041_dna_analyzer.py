# ==============================================================================
# 🚀 PROJECT: DNA GC Content Analyzer
# Objective: Implement the function(s) from scratch to pass all tests.
# ==============================================================================

def gc_content(dna_sequence: str) -> float:
    # Return percentage of 'G' and 'C' bases rounded to 1 decimal place
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
assert gc_content("ATGC") == 50.0, "Test 1 Failed"
assert gc_content("GGCC") == 100.0, "Test 2 Failed"
print("🏆 PROJECT 041 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
