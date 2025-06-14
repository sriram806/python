"""String Method are use to manipulate the strings"""

name = input("Please Enter any String: ")

#to find length of the string we use len()
length = len(name)
print(f'The Total letters in {name} is {length}')

#to find any letter position we use find()
#from begining of string
letter = "i"
b_position = name.find(letter)
print(f'The letter {letter} in {name} is at {b_position}')

#from backside means end-side we use rfind()
letter = "S"
l_position = name.rfind(letter)
print(f'The letter {letter} in {name} is at {l_position}')

#To Capatilize a string we use capitilize()

capitilize= name.capitalize()
print(f"Your {name} has been Capitilized and become {capitilize}")

#to Upper the string we use upper()

upper = name.upper()
print(f'Your {name} has been Upperized and become {upper}')

#to Lower the string we use lower()

lower = name.lower()
print(f'Your {name} has been Upperized and become {lower}')

# To find the string contain numbers we use isdigit()

digit = name.isdigit()
print(f"Your {name} is number: {digit} ")

# To find the string contain only characters we use isalpha()

alpha = name.isalpha()
print(f"Your {name} is number: {alpha} ")


#To count any strings we use count()
string_that_count = "S"
count= name.count(string_that_count)
print(f'In your {name} There are total {count} {string_that_count} are present ')

#Exersise

username = input("Enter your username: ")

if len(username) >= 12:
    print("Username does't contain more than 12 characters")
elif not username.find(' ') == -1:
    print("Username doesn't conatin any spaces")
elif not username.isdigit:
    print("Username doesn't contain any numbers")
else:
    print(f"Welcome {username}")