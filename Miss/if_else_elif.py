chochlates=6
num= int(input('enter number of chochlates needed:'))
if num<=chochlates and num>0:
    print("Please collect chochlates")
elif num==chochlates:
    print("Please collect chochlates")
elif num>chochlates:
    print("Sorry! the given number of chochlates are not available.")
    print(f"Availble chochlates count:{chochlates}")
else:
    print('Invalid number')
