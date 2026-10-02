class CalculatorAgent:

    def calculate(self, command):

        parts = command.lower().split()

        if len(parts) != 3:
            return "Use: add 10 5"

        operation = parts[0]

        try:
            a = float(parts[1])
            b = float(parts[2])
        except ValueError:
            return "Please enter valid numbers."

        if operation == "add":
            return a + b

        if operation == "subtract":
            return a - b

        if operation == "multiply":
            return a * b

        if operation == "divide":

            if b == 0:
                return "Cannot divide by zero."

            return a / b

        return "Unknown operation. Use add, subtract, multiply, or divide."