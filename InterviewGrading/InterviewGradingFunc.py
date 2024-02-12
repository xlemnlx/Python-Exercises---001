def InterviewGrading (testVariable):
    interviewDuration = testVariable[-1]
    examsDuration = testVariable[0]
    
    output = None
    
    examsDurationLimit = [5, 5, 10, 10, 15, 15, 20, 20]
    
    if interviewDuration <= 120:
        interviewGrade = True
    else:
        interviewGrade = False
        
    if len(examsDuration) < len(examsDurationLimit):
        examGrade = False
    else:
        for indx, i in enumerate(examsDuration):
            if i <= examsDurationLimit[indx]:
                examGrade = True
            else:
                examGrade = False
                break
                
    if interviewGrade is True and examGrade is True:
        output = "qualified"
    else:
        output = "disqualified"
    
    return output