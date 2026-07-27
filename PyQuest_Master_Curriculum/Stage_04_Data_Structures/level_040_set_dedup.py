# ==============================================================================
# LEVEL: Deduplicating Lists with Set
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
duplicates = [1, 1, 2, 2, 3]
unique_items = list(set(___))


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert sorted(unique_items) == [1, 2, 3], "unique_items must equal [1, 2, 3]"
    print("🎉 LEVEL CLEARED! Mastered: Deduplicating Lists with Set")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
