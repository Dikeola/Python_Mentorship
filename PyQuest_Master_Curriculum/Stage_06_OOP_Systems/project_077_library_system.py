# ==============================================================================
# 🚀 PROJECT: Library Management System
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    # Implement add_book(book), checkout_book(title) -> bool
    pass


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
b = Book("Python 101", "Author")
lib = Library()
lib.add_book(b)
assert lib.checkout_book("Python 101") is True, "Test 1 Failed"
assert lib.checkout_book("Python 101") is False, "Test 2 Failed"
print("🏆 PROJECT 077 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
