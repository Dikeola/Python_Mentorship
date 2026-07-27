# ==============================================================================
# ⚔️ BOSS FIGHT: Fix Missing Self Argument in Class Methods
# Task: Debug and fix the broken code below so it passes validation!
# ==============================================================================

# --- BROKEN CODE ---
# Fix this class method definition so it doesn't fail with TypeError when called
class Wizard:
    def __init__(self, name):
        self.name = name
    # Fix method signature below
    def cast_spell():
        return "Fireball!" 


# --- BOSS VALIDATION (Do not edit below) ---
try:
    assert Wizard('Gandalf').cast_spell() == 'Fireball!', "Self argument check failed"
    print("⚔️ BOSS DEFEATED! You fixed the code.")
except AssertionError as e:
    print(f"❌ BOSS DEFEATED YOU: {e}")
except Exception as e:
    print(f"❌ CODE ERROR: {e}")
