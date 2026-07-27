# ==============================================================================
# LEVEL: Ternary Operator
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
is_vip = True
discount = 20 if is_vip else ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert discount == 20, "discount must equal 20"
    print("🎉 LEVEL CLEARED! Mastered: Ternary Operator")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
