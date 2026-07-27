# ==============================================================================
# 🚀 PROJECT: API Exception Hierarchy Handler
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class BaseAPIException(Exception):
    status_code = 500

class NotFoundError(BaseAPIException):
    status_code = 404

class UnauthorizedError(BaseAPIException):
    status_code = 401

def handle_exception(exc: BaseAPIException) -> dict:
    # Return {"error": exc.__class__.__name__, "status": exc.status_code}
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
err = NotFoundError("Item missing")
assert handle_exception(err) == {"error": "NotFoundError", "status": 404}, "Test 1 Failed"
print("🏆 PROJECT 102 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
