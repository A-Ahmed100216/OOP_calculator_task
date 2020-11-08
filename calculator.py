# Create a class called Calculator
class Calculator:
    # Initialise so as to take user input for numbers
    def __init__(self):
        # Display message
        self.display=print("Calculator Programme. Please enter numbers only.")


    # Define an operations function
    def operations(self):
        # Take user input, guiding user to follow certain input so the split method is effective
        self.input = input("Please enter your calculation separated with spaces (e.g. 12 * 37)  ").split()
        # Identify number 1, number 2, and the operator.
        self.num1 = int(self.input[0])
        self.num2 = int(self.input[-1])
        self.operation=self.input[1]
        # Depending on the operator, perform the corresponding operation
        if self.operation == "+":
            result= self.num1 + self.num2
        elif self.operation == "-":
            result= int(self.num1) - self.num2
        elif self.operation == "*":
            result= int(self.num1) * self.num2
        elif self.operation == "/":
            result= int(self.num1) / self.num2
        # If the operator is invalid, ask to re-enter
        else:
            return input("Invalid operation, please try again")

        return result
    # Create divisble_by function
    def divisible_by(self):
        # Ask user to input number 1 and number 2
        self.num1 = int(input("Please enter number 1: "))
        self.num2 = int(input("Please enter number 2: "))
        print("{} is divisible by {}?".format(self.num1, self.num2))
        # If divisble, return True, otherwise, False
        if self.num1 % self.num2 == 0:
            return True
        else:
            return False

    # Create area function.
    def area(self):
        # Ask user to input height and length
        self.length = int(input("Please enter length: "))
        self.height = int(input("Please enter height: "))
        result = (self.length * self.height) / 2
        # Return as a formatted string
        return "The area of a right-angle triangle with sides {} units by {} units is {} units squared ".format(self.length,self.height,result)


    # Create converter method
    def converter(self):
        # Ask user to input the number they wish to convert
        self.number = int(input("Converter cm-->inches  \nPlease enter the number you wish to convert: "))
        result = int(self.number) / 2.54
        # Return as a formatted string
        return "{}cm is equivalent to {} inches.".format(self.number, result)