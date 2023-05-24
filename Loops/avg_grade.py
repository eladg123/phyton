# מקבלים רשימת ציונים ומחשבים ממוצע של רק מי שקיבל מ60 ומעלה

def avg_grade(lst):
    sum = 0
    students_counter = 0
    for grade in lst:
        print(grade)
        if grade >= 60:
            students_counter = students_counter+1
            sum = sum+grade
    return sum/students_counter


print(avg_grade([60,65]))