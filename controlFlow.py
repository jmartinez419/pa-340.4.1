x = 7
if(x<10):
    print("Less than 10")



x = 7 

if(x<10):
    print("Less than 10")
else: print("Greater than 10")


x = 21

if(x<10):
    print("less than 10")
elif(x> 10 and x< 20):
    print("Between 10 and 20")
else: print("Greater than or equal to 20")


x = 5

if(x < 10 or x > 20):
    print("Out of range")
else: print("In range")

score = int(input("Enter your Score: "))

if(score >= 90 and score <= 100):
    print("A: " + str(score))
elif(score >= 80 and score <= 89):
    print("B: " + str(score))
elif(score >= 70 and score <= 79):
    print("C: " + str(score))
elif(score >= 60 and score <= 69):
    print("D: " + str(score))
elif(score < 60 and score >= 0): 
    print("F: " + str(score))
else:print("Score out of range.")