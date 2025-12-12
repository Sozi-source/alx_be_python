class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b 

print(Calculator.add(4, 6))

result = Calculator.multiply(4, 6)
print(f"Result: {result}")
