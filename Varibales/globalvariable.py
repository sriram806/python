"""x = "Sriram"
def myfunction():
    print(x)

myfunction()"""

x = "Sriram"
def myfunction():
    global x
    x = "guru"
    print(x)
    
myfunction()

print(x)