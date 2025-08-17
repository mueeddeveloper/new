amount =int(input("enter the amount of notes"))
note_100 = amount //100 
note_50 = (amount %100) // 50
note_10 = ((amount % 100)%50) //10
print("Number of 100 notes:", note_100)
print("Number of 50 notes:", note_50)
print("Number of 10 notes:", note_10)