# ==============================================================================
# 🚀 PROJECT: Sliding Window Rate Limiter
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        # Track client request timestamps
        pass

    def allow_request(self, client_id: str) -> bool:
        # Return True if client_id has made less than max_requests in past window_seconds
        pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
limiter = RateLimiter(max_requests=2, window_seconds=1.0)
assert limiter.allow_request("client_A") is True, "Test 1 Failed"
assert limiter.allow_request("client_A") is True, "Test 2 Failed"
assert limiter.allow_request("client_A") is False, "Test 3 Failed"
print("🏆 PROJECT 097 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
