test_list = [
	"increasing", "adventures", "enticing", "unacceptable", "accountable", "incredible", "exquisite",
	"am", "enduring", "outstanding", "astonishing", "astounding", "impressive", "revolutionize",
	"recurring", "recollection", "so", "gorgeous", "captivating"
]

def StutteringFunc(list_of_words):
    
    for i in list_of_words:
        stut = i[0] + i[1] + "..."
        stuttering = stut + " " + stut + " " + i + "?"
        print(stuttering)
        
StutteringFunc(test_list)