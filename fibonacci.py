def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci sequence:", fibonacci_sequence(num))
    except ValueError:
        print("Invalid input! Please enter an integer.")