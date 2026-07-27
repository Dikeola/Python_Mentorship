# ==============================================================================
# 🚀 PROJECT: Polymorphic Vehicle Rental
# Objective: Implement the function(s)/class(es) from scratch to pass all tests.
# ==============================================================================

class Vehicle:
    def __init__(self, daily_rate: float):
        self.daily_rate = daily_rate
    def calculate_rental(self, days: int) -> float:
        return self.daily_rate * days

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def calculate_rental(self, days: int) -> float:
        # Truck includes $50 flat fee
        return super().calculate_rental(days) + 50.0


# --- AUTOMATED TEST SUITE (Do not edit below) ---
try:
c = Car(40.0)
t = Truck(80.0)
assert c.calculate_rental(2) == 80.0, "Test 1 Failed"
assert t.calculate_rental(2) == 210.0, "Test 2 Failed"
print("🏆 PROJECT 081 CLEARED!")
except NameError as e:
    print(f"❌ PROJECT FAILED: Missing function, class, or variable name - {e}")
except AssertionError as e:
    print(f"❌ PROJECT FAILED: {e}")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
