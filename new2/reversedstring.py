string = input("please enter a string:")
string2 =('')
for i in string:
    string2 = i + string2
    print("\nthe original string is:",string)
    print("\nthe reversed string is:",string2)