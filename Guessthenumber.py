from random import randint as a
print("Guess the Number!!")
b = input(int())
if a(1, 9) == b:
    print("Correct the Number is %d" % (b))
else:
    print("That's not the number")


