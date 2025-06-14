"""conditional_expression = a one line statement that shortcut the if-else statement using print or if-else"""

#Lets check with example (check it is number positive or negative)
number = -10
print("The Number is Positive" if number > 0 else "The Number is Negative")

#Lets check with another example (check the number is even or odd)
number = 20
result = "EVEN" if number % 2 == 0 else "ODD"
print(f'The {number} is {result} Number')

#Lets check with another example to find maximum and minimun value 
number1=10
number2=100
maximun= number1 if number1 > number2 else number2
minimum= number1 if number1 < number2 else number2

print(f"Among the Numbers {number1} and {number2} , {maximun} is bigger!")
print(f"Among the Numbers {number1} and {number2} , {minimum} is Smaller!")

#Lets check with another example to handle strings

user_role = 'admin'

result = "Full Access" if user_role == 'admin' else "Limited Access"

print(f"You are {user_role},so you have {result}")