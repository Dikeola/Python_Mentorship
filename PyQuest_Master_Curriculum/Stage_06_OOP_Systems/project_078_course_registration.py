# ==============================================================================
# 🚀 PROJECT: Course Enrollment System
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Course:
    # Implement __init__(name, capacity), enroll_student(student_name) -> bool
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
c = Course("CS101", 1)
assert c.enroll_student("Alice") is True, "Test 1 Failed"
assert c.enroll_student("Bob") is False, "Test 2 Failed"
print("🏆 PROJECT 078 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
