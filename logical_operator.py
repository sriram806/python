"""logical_operator = evaluates multiple conditions 
 or - at least one condtion must be true 
 and - both conditions must be true
 not - it invert the condition if it is true then it is false """

print("using or condition:")
temp = 20
isRaining = False

if temp> 35 or temp < 0 or isRaining:
    print("The Outdoor event is cancelled")
else:
    print("The Outdoor event is Still Scheduled")


print("using and condition:")

temp= -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("Today is Hot and Sunny at outside")
elif temp <= 0 and is_sunny:
    print("Today is Cold and Sunny at outside")
elif 28 > temp > 0 and is_sunny:
    print("Today is Warm and sunny at outside")
    

print("using not condition:")

temp = 20
is_sunny= False

if temp >=28 and is_sunny:
    print("Today is Hot and sunny at outside")
elif temp <=0 and is_sunny:
    print("Today is COLD and sunny at outside")
elif 28 > temp > 0 and is_sunny:
    print("Today is WARM and sunny at outside")
elif temp >=28 and not is_sunny:
    print("Today is Hot and Cloudy at ouside")
elif temp <=0 and not is_sunny:
    print("Today is COLD and Cloudy at outside")
elif 28 > temp >0 and not is_sunny:
    print("Today is WARM and Cloudy at outside")
    
