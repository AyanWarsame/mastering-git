"""
Simple Calculator for practicing Git operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def main():
    """Main function"""
    print("=== Simple Calculator ===")
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            else:
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()
