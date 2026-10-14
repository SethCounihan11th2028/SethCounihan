print("Behold the great fortune teller Bob!!!!!! \n ")
print("The great Bob will now ask you questions to predict your future!!!!!! \n")

def fortune():
    try:
        lucky = int(input("What is your lucky number!!!!!!!!!! \n"))
        number = int(input("Give a number!!!!!!! \n"))
        numbre = int(input("What is another number!!!!!!!!!!! \n"))
        random = int(input("Give a number between 1 and 100!!!!!!!!! \n"))
        if lucky + number + numbre + random > 100:
            print("You will buy a new pair of pants.")
        elif lucky + number + numbre + random <= 100:  
            print("You will get hit by a bus.")
        elif lucky + number + numbre + random <= 75:
            print("You will find love.")
        elif lucky + number + numbre + random <= 50:
            print("You will win the lottery.")
        elif lucky + number + numbre + random <= 25:
            print("You will get a hangnail.")
    except:
          print("Try Again \n ")
          fortune()


fortune()




'''
try: 
    lucky turn into int/float
    number
    
    random turn into int/float
except:
    run again
'''