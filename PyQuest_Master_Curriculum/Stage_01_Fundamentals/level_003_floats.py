# ==============================================================================
# LEVEL: Float Types
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
price = ___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert isinstance(price, float) and price == 19.99, "price must be float 19.99"
    print("🎉 LEVEL CLEARED! Mastered: Float Types")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
