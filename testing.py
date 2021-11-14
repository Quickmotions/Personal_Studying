# modulus test

print(10 % 3)  # 10/ 3 = 1 reminainder so prints 1
print(2 % 5)

# 4 % 2 means "2 divided by 2 is what, and what is the remainder? if I have a remainder, return it or else return 0"
if 4 % 2 == 0:
    print("2 is even")
else:
    print("2 is odd")

# Example of modulo operator with negative numbers


rem1 = -18 % -3

rem2 = -25 % 5

rem3 = 30.6 % -6

rem4 = -35.5 % -5.5

print("Remainder of -18 % -3 = ", rem1)

print("Remainder of -25 % 5 = ", rem2)

print("Remainder of  30.6 % -6 = ", rem3)

print("Remainder of -35.5 % -5.5 = ", rem4)