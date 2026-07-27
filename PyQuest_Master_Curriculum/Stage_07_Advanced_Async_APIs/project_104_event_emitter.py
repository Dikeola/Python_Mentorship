# ==============================================================================
# 🚀 PROJECT: Pub-Sub Event Emitter
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class EventEmitter:
    # Implement on(event_name, callback), emit(event_name, *args)
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
events = EventEmitter()
logs = []

events.on("user_login", lambda user: logs.append(f"Login: {user}"))
events.emit("user_login", "Alice")

assert logs == ["Login: Alice"], "Test 1 Failed"
print("🏆 PROJECT 104 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
