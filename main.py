from method import karatsuba;

# Main function
def main():
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = karatsuba(num1, num2)

    print(f"The result of multiplying {num1} and {num2} using the Karatsuba algorithm is: {result}.")

if __name__ == "__main__":
    main()