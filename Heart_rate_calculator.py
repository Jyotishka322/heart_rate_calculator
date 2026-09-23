# Heart_rate_calculator.py
# this is a simple program to calculate a person's heart rate in BPM
# Formula used: heart rate = (beats/time)*60
#======================================================================
print("***********************************************************")
print("           Heart Rate Calculator                       ")
print("***********************************************************")
print("this program is to calculate a person's heart rate in BPM")
print("BPM means Beats Per minute")


name = input("enter your name:")


print("hello", name+"!")
print("now we will start calculating your heart rate in BPM")


# Give your approximate number of heartbeats counted and the time in secomds it took to count those heartbeats.

try:
    beats = int (input("enter the number of heartbeats counted :"))
    time = int(input("enter the time in seconds:"))

    if beats <0:
        print("\ninvalid input! ")

    elif time<=0:
        print("\ninvalid input!")

# calculating heart rate using the formula in BPM
    else:
        heart_rate = (beats/time)*60

        
        print("***********************************************************")
        print("       YOUR RESULT        ")
        print("***********************************************************")
        print("name:",name)
        print("heartbeats counted:",beats)
        print("time:",time,"seconds")
        print("heart rate:",round(heart_rate,2),"BPM")
        print("***********************************************************")
        

        if heart_rate<60:
            print("your heart rate is below 60BPM")
            print("this is conisidered a low resting heart rate")

        elif heart_rate<=100:
            print("your heart rate is between the range of 60 and 100 BPM")
            print("this is a typical rersting heart rate range for many adults")

        else:
            print("your heart rate is above 100 BPM")
            print("this is considered as high resting heart rate")

        
        print("***********************************************************")
        print("          FORMULA USED                ")
        print("***********************************************************")
        print("heart rate = (beats/time)*60")
        print()
        print("your calculation:")
        print("heart rate =(",beats,"/",time,")*60")
        print("heart rate =",round(heart_rate,2),"BPM")
        print("***********************************************************")

except ValueError:
    print("\ninvalid input! enter valid input for the number of beats and time in seconds")        


print("thanks for using this program")
print("have a nice day",name+"!")