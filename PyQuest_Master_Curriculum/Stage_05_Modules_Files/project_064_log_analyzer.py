# ==============================================================================
# 🚀 PROJECT: HTTP Server Log Analyzer
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

def count_status_codes(log_text: str) -> dict:
    # Parse lines like "GET /index.html 200" and count occurrences of each status code (e.g. 200, 404)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
logs = "GET / 200\nGET /about 404\nPOST /login 200"
assert count_status_codes(logs) == {200: 2, 404: 1}, "Test 1 Failed"
print("🏆 PROJECT 064 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
