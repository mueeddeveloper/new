medical_cause=input("did you have any medical cause yes or no")
atten =int(input("enter the attendance of the student"))
if medical_cause == "yes":
    print("you are allowed")
else:
    if atten >= 75:
        print("you are allowed")
    else:
        print("not allowed")