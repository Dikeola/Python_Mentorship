# ==============================================================================
# 🚀 PROJECT: Dotenv Line Parser
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def parse_env_text(env_text: str) -> dict:
    # Parse KEY=VAL strings, ignoring blank lines and lines starting with '#'
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
env = "# Comment\nPORT=8080\nHOST=localhost"
assert parse_env_text(env) == {"PORT": "8080", "HOST": "localhost"}, "Test 1 Failed"
print("🏆 PROJECT 074 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
