# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Off-By-One String Slice
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix string slicing so result contains the full word 'Python'
text = "Python Programming"
# Slicing was stopping 1 index too early
python_word = text[0:5]


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert python_word == 'Python', "python_word must equal 'Python'"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
