class InvalidOperationError(Exception):
    pass


while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operator = input("Enter an operation (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise InvalidOperationError("Unsupported operator!")

        print("Result:", result)
        break

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError as e:
        print("Error:", e)

    except InvalidOperationError as e:
        print("Error:", e)

    finally:
        print("Calculation attempt completed.\n")

print("Calculator finished!")