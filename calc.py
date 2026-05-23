"""
Simple Calculator for practicing Git operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def main():
    """Main function"""
    print("=== Simple Calculator ===")
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    
    choice = input("\nEnter your choice (1, 2 or 3): ").strip()
    
    if choice in ['1', '2', '3']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            else:
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
