def check_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if original == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
def check_armstrong(n):
    original = n
    digits = 0
    temp = n

    while temp > 0:
        digits += 1
        temp = temp // 10

    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if original == total:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    print("Reversed Number:", rev)
def sum_and_count_digits(n):
    count = 0
    total = 0

    if n == 0:
        count = 1
    else:
        while n > 0:
            digit = n % 10
            total += digit
            count += 1
            n = n // 10

    print("Number of digits:", count)
    print("Sum of digits:", total)
#Menu
while True:
    print("\n--- Number Analyzer ---")
    print("1. Palindrome Check")
    print("2. Armstrong Check")
    print("3. Reverse Number")
    print("4. Sum and Count of Digits")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting program")
        break

    n = int(input("Enter a number: "))

    if choice == 1:
        check_palindrome(n)
    elif choice == 2:
        check_armstrong(n)
    elif choice == 3:
        reverse_number(n)
    elif choice == 4:
        sum_and_count_digits(n)
    else:
        print("Invalid choice")