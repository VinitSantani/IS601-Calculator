from Function import *


class Calculator:
    result=0;
    
    def __init__(self):
        pass

    def add(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result






# print("Please select operation -\n" \
#       "1. Add\n" \
#       "2. Subtract\n" \
#       "3. Multiply\n" \
#       "4. Divide\n" \
#       "5. Square\n"\
#       "6. SquareRoot\n" )

# # Take input from the user
# select = int(input("Select operations form 1, 2, 3, 4 ,5, 6:"))

# number_1 = int(input("Enter first number: "))
# if select != 5 or select !=6:
#     number_2 = int(input("Enter second number: "))

# if select == 1:
#     print(number_1, "+", number_2, "=",
#           add(number_1, number_2))

# elif select == 2:
#     print(number_1, "-", number_2, "=",
#           subtract(number_1, number_2))

# elif select == 3:
#     print(number_1, "*", number_2, "=",
#           multiply(number_1, number_2))

# elif select == 4:
#     print(number_1, "/", number_2, "=",
#           divide(number_1, number_2))

# elif select == 5:
#     print(number_1, "^" , 2 , "=",
#         square(number_1), sep="")

# elif select == 6:
#      print(number_1, "^" , 0.5 , "=",
#         sqrt(number_1), sep="")

# else :
#     print("Invalid input")