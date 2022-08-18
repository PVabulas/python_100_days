import art


def calculator():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    def continue_calc(num1):
        operation = input(
            f"Using {num1}, which operation do you want? ({', '.join(list(operations.keys()))})\n"
            + "Type 'q' to quit.\n"
        )
        if operation == "q":
            return "q"
        else:
            num2 = float(input("What's the next number?\n"))
            answer = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {answer}")
            return answer

    print(art.logo)
    num1 = float(input("What's the first number?\n"))
    operation = input(
        f"Which operation do you want? ({', '.join(list(operations.keys()))})\n"
    )
    num2 = float(input("What's the second number?\n"))
    answer = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    while True:
        answer = continue_calc(answer)
        if answer == "q":
            break
    print("Goodbye!")
