# ==============================================================================
# 🚀 PROJECT: Validated User Profile Dataclass
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

from dataclasses import dataclass

@dataclass
class UserProfile:
    username: str
    email: str
    age: int

    # Implement __post_init__ to raise ValueError if age < 0 or '@' not in email
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
try:
    UserProfile("alice", "invalid_email", 25)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

u = UserProfile("bob", "bob@example.com", 30)
assert u.username == "bob", "Test 1 Failed"
print("🏆 PROJECT 095 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
