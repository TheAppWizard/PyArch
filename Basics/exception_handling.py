def math():
    try:
        # Get user input
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Convert inputs to integers
        num1 = int(num1)
        num2 = int(num2)

        # Perform arithmetic operations
        sum_result = num1 + num2
        difference_result = num1 - num2
        product_result = num1 * num2
        division_result = num1 / num2

        # Display results
        print("Sum:", sum_result)
        print("Difference:", difference_result)
        print("Product:", product_result)
        print("Division:", division_result)

    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Arithmetic operations performed successfully.")
    finally:
        print("End of arithmetic operation.")

# Example usage
math()
