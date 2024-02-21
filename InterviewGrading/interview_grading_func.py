def interview_grading (test_variable):
    interview_duration = test_variable[-1]
    exams_duration = test_variable[0]
    
    output = None
    
    exams_duration_list = [5, 5, 10, 10, 15, 15, 20, 20]
    
    if interview_duration <= 120:
        interview_grade = True
    else:
        interview_grade = False
        
    if len(exams_duration) < len(exams_duration_list):
        exam_grade = False
    else:
        for indx, i in enumerate(exams_duration):
            if i <= exams_duration_list[indx]:
                exam_grade = True
            else:
                exam_grade = False
                break
                
    if interview_grade is True and exam_grade is True:
        output = "qualified"
    else:
        output = "disqualified"
    
    return output