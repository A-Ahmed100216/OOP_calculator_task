# Exercise - OOP Calculator

### Summary
Build a basic Object Oriented Calculator
### Tasks
1. Build a simple calculator class containing add, subtract, multiply, divide.
2. Expand by creating:
   * Divisible by method that returns true or false dependent on the outcome.
   * Work out and return the area of a triangle.
   * inch to cm converter.

### Acceptance Criteria
* New Project and Repository
* At least 5 commits 
* Uses OOP - must be in class and method format
* Has documentation
* Follows best practices


# Process

#### 1. Create class
A parent class called Calculator was created. This was initialised to display a simple message.

```python
class Calculator:
    # Initialise so as to take user input for numbers
    def __init__(self):
        self.display=print("Calculator Programme. Please enter numbers only.")
```

* An operations function defines the execution of basic mathematics operators. 
* The user inputs their entire calculation, as such is the case with a normal calculator. The user is told to seperate with spaces as the split method is used to create a list with which number 1, number 2 and the operator can be identified. 
* Control flow is used to determine the type of operator so the subsequent operation can be performed 
```python
    # Define an operations function
    def operations(self):
        self.input = input("Please enter your calculation separated with spaces (e.g. 12 * 37)  ").split()
        self.num1 = int(self.input[0])
        self.num2 = int(self.input[-1])
        self.operation=self.input[1]
        if self.operation == "+":
            result= self.num1 + self.num2
        elif self.operation == "-":
            result= int(self.num1) - self.num2
        elif self.operation == "*":
            result= int(self.num1) * self.num2
        elif self.operation == "/":
            result= int(self.num1) / self.num2
        else:
            return input("Invalid operation, please try again")

        return result
```
* The next method defined is divisible by which returns True or False as to whether the first number is divisible by the second. 
```python
    def divisible_by(self):
        self.num1 = int(input("Please enter number 1: "))
        self.num2 = int(input("Please enter number 2: "))
        print("{} is divisible by {}?".format(self.num1, self.num2))
        if self.num1 % self.num2 == 0:
            return True
        else:
            return False
```
* The area method is designed to return the area of a right-angled traingle, given the height and length. 
```python
    def area(self):
        self.length = int(input("Please enter length: "))
        self.height = int(input("Please enter height: "))
        result = (self.length * self.height) / 2
        return "The area of a right-angle triangle with sides {} units by {} units is {} units squared ".format(self.length,self.height,result)

```
* The final method is a convertor which simply converts fromm cm to inches. 
```python
    def converter(self):
        self.number = int(input("Converter cm-->inches  \nPlease enter the number you wish to convert: "))
        result = int(self.number) / 2.54
        return "{}cm is equivalent to {} inches.".format(self.number, result)
```
#### 2. Instantiation
* The class is instantiated in a separate run file. The Calcualtor class must be imported first. 
```python
from calculator import Calculator
```
* The class is instantiated as a variable called calc_test. Each of the method are called to test.
```python
calc_test=Calculator()
print(calc_test.operations())
print(calc_test.divisible_by())
print(calc_test.area())
print(calc_test.converter())
```
