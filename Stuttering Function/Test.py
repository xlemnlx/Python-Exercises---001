testList = [
	"increasing", "adventures", "enticing", "unacceptable", "accountable", "incredible", "exquisite",
	"am", "enduring", "outstanding", "astonishing", "astounding", "impressive", "revolutionize",
	"recurring", "recollection", "so", "gorgeous", "captivating"
]

def StutteringFunc(listOfWords):
    
    for i in listOfWords:
        stut = i[0] + i[1] + "..."
        stuttering = stut + " " + stut + " " + i + "?"
        print(stuttering)
        
StutteringFunc(testList)