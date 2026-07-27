# ==============================================================================
# LEVEL: Private Encapsulation Convention
# Task: Replace '___' with the correct code to clear the level!
# ==============================================================================

# --- YOUR TRIAL ---
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def get_balance(self):
        return self.___


# --- LEVEL VALIDATION (Do not edit below) ---
try:
    assert BankAccount(100).get_balance() == 100, "Encapsulation check failed"
    print("🎉 LEVEL CLEARED! Mastered: Private Encapsulation Convention")
except AssertionError as e:
    print(f"❌ LEVEL FAILED: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
