x = float(float(input("enter the acutual price you bought at")))
sell = float(float(input("enter the selling price")))
if x<sell:
    amount = sell - x
    print("total profit is", amount)
else:
    print("no profit")
    
