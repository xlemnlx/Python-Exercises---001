from UncensoredStringFunc import UncensoredString

testOne = ("Wh*r* d*d my v*w*ls g*?", "eeioeo")
testTwo = ("abcd", "")
testThree = ("*PP*RC*S*", "UEAE")
testFour = ('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee')
testFive = ('*l*ph*nt', 'Eea')

UncensoredString(testOne)
UncensoredString(testTwo)
UncensoredString(testThree)
UncensoredString(testFour)
UncensoredString(testFive)