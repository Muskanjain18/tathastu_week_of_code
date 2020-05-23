cp=float(input("Enter Cost Price of product: "))
sp=float(input("Enter Selling Price of product: "))
profit=sp-cp
sp1=cp+profit+(0.05*profit)
print("Profit from this sell:",profit)
print("To increase profit by 5% the selling price should be:",sp1)
