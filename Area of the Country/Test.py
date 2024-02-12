def AreaOfCountry(countryArea):
    earthArea = 148940000
    percentage = round(((countryArea[1] / earthArea) * 100), 2)
    strOut = countryArea[0] + " is " + str(percentage) + "% of the total world's landmass."
    return strOut

testOne = ("Russia", 17098242)
testTwo = ("USA", 9372610)
testThree = ("Iran", 1648195)

print(AreaOfCountry(testOne))
print(AreaOfCountry(testTwo))
print(AreaOfCountry(testThree))