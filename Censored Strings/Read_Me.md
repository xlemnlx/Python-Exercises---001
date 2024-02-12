From: https://edabit.com/challenge/zJSF5EfPe69e9sJAc
Difficulty: Hard

Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples:

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*") ➞ "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

censor_string("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!") ➞ "!!! do my cats !!!! !!!!!! grass?")
censor_string("How do I stop myself from using python!?", ["do", "stop", "using"], "-") ➞ "How -- I ---- myself from ----- python!?")
censor_string("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~") ➞ "If ~~~~~~~~~~~~~~~~~~~~ are ~~~~~~~~~~~~ fun ~~~~ use.")
censor_string("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?") ➞ "I'm dyslexic, but ???? deos'tn ???????")
censor_string("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*") ➞ "I ****** be doing work *** I am doing **** instead.")


testOne = ("Today is a Wednesday!", ["Today", "a"], "-")
testTwo = ("The cow jumped over the moon.", ["cow", "over"], "*")
testThree = ("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*")
testFour = ("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!")
testFive = ("How do I stop myself from using python!?", ["do", "stop", "using"], "-")
testSix = ("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~")
testSeven = ("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?")
testEight = ("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*")