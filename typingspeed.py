from time import *
import random as r  
#for error detection between user input and the paragraph from our string we are making function
def mistake(paragraph_test,user_test):
    error=0
    for i in range(len(paragraph_test)):
        try:
            if(paragraph_test[i]!=user_test[i]):           
                error=error+1
        except:
            error=error+1
    return error
def speed(time_s,time_e,user_input):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(user_input)/time_R
    return round(speed,2)
while True:
    ask=input("ARE YOU READY TO TEST:YES/NO")
    if(ask=="YES"):
        test=["My name is khushali","My age is 21",
      "I am from bhopal"]
        test1=r.choice(test)
        print(test1)
        print("*****  TYPING SPEED  *****")
        time_1=time()                                       #it calculates the time before input
        testinput=input("Enter :  ")
        time_2=time()                                       #it calculates the time after input

        #NOW we want to two things:
        #typing speed calculation
        #error in the string
        print("Speed :",speed(time_1,time_2,testinput))
        print("Errors:",mistake(test1,testinput))
    elif(ask=="NO"):
        print("THANKYOU")
        break
    else:
        print("WRONG INPUT")



