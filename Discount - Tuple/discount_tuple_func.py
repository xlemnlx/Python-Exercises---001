def discount_tuple(varTuple):
    discount = varTuple[0] - (varTuple[0] * (varTuple[1] / 100))
    return(int(discount) if int(discount) == discount else float("{:.2f}".format(discount)))
    # {:.2f} . format returns the first two decimal of the answer.