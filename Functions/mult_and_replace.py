# הפונקציה סופרת כמה סימני קריאה מופיעים במחרוזת
# משרשמרת את המחרוזת לעצמה כמספר סימני הקריאה שנספרו
# מחליפה במחרוזת החדשה את סימני הקריאה בסימני שאלה ומחזיקה את התוצאה
# אם אין המחרוזת סימני קריאה יש להחזיר את המחרוזת ריקה

def mult_and_replace(str):
    times = str.count("!")
    if times==0:
        return ""
    str = str*times
    str = str.replace("!",'?')
    return str

print(mult_and_replace("Hey! what is up!!!"))