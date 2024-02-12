from CensoredStringFunc import CensoredString

testOne = ("Today is a Wednesday!", ["Today", "a"], "-")
testTwo = ("The cow jumped over the moon.", ["cow", "over"], "*")
testThree = ("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*")
testFour = ("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!")
testFive = ("How do I stop myself from using python!?", ["do", "stop", "using"], "-")
testSix = ("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~")
testSeven = ("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?")
testEight = ("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*")

print(CensoredString(testOne))
print(CensoredString(testTwo))
print(CensoredString(testThree))
print(CensoredString(testFour))
print(CensoredString(testFive))
print(CensoredString(testSix))
print(CensoredString(testSeven))
print(CensoredString(testEight))