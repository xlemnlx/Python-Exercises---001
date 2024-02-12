varOne = (1500, 50)     # 750
varTwo = (89, 20)       # 71.2
varThree = (100, 75)    # 25

def DiscountOnTuple(varTuple):
    discount = varTuple[0] - (varTuple[0] * (varTuple[1] / 100))
    return(int(discount) if int(discount) == discount else discount)
    # This will remove the decimal if its "0" since the int(variable) is equal to the float(variable). 
    # If it's not, then it will print the decimal because of the else statement.

print(DiscountOnTuple(varOne))
print(DiscountOnTuple(varTwo))
print(DiscountOnTuple(varThree))