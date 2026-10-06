word_one = input("What is the first word? \n ")
word_two = input("What is the second word? \n ")
word_three = input("What is the third word? \n ")

print(word_one + word_two + word_three)


int_one = int(input("What is the first integer? \n "))
int_two = int(input("What is the second integer? \n "))
int_three = int(input("What is the third integer? \n "))

def add_three(a, b, c):
    print(a + b + c)

add_three(int_one, int_two, int_three)


def data_three():
    word = input("What is the word? \n ")
    integer = int(input("What is the integer? \n "))
    floater = float(input("What is the float? \n "))
    print(word + str(integer)+ str(floater))

data_three()