# Create a class called Calculator
class Calculator:
    # Initialise so as to take user input for numbers
    def __init__(self):
        self.num1=int(input("Please enter number 1: "))
        self.num2=int(input("Please enter number 2: "))

        # Check the inputs are numbers
        # while self.num1==str:
        #     return input("Invalid input, please try again:  ")
    # Define an operations function
    def operations(self):
        self.operation=input("What operation would you like to perform: ").lower()
        if self.operation =="add" or self.operation=="addition" or self.operation=="+":
            result= self.num1 + self.num2
        elif self.operation =="subtract" or self.operation=="subtraction" or self.operation=="minus" or self.operation=="-":
            result= self.num1 - self.num2
        elif self.operation =="multiply" or self.operation=="multiplication" or self.operation=="times" or self.operation=="*" or self.operation=="x":
            result= self.num1 * self.num2
        elif self.operation =="divide" or self.operation=="division" or self.operation=="div" or self.operation=="/" :
            result= self.num1 / self.num2
        else:
            return input("Invalid operation, please try again")

        return result


calc_test=Calculator()
print(calc_test.operations())