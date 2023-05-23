
def final_grade(exam,hw):
    result=0
    if exam>=50 and hw<exam+25:
        result = (exam/100*75) + (hw/100*25)
        return round(result)
    else:
        result = exam
        return round(result)


print(final_grade(90,79.4))