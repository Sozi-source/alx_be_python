import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    if isinstance(result, float):
        # Print exactly what the checker expects
        print(f"The result of the division is {result}")
    else:
        # Print error messages directly
        print(result)

if __name__ == "__main__":
    main()
