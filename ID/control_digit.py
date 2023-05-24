# פונקציה לחישוב ספרת ביקורת של תז
# הקלט הוא תז ללא ספרת ביקורת, זאת אומרת 8 ספרות
def control_digit(ID):
    s = 0
    for i in range(8):
        digit = int(ID[i])
        if i % 2 == 0:                # בדיקה אם האינדקס במיקום זוגי או לא
            s = s+digit
        else: 
            digit = digit * 2
            if digit <=9:
                s = s + digit
            else:
                ones = digit%10
                tens = 1
                s = s + ones + tens
    ones_of_s = s%10
    check_digit = 10 - ones_of_s
    if check_digit == 10:
        check_digit = 0
    return check_digit


print(control_digit("73908547"))