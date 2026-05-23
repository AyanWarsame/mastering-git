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
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")


if __name__ == "__main__":
    main()
