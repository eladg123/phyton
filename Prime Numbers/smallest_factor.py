# פונקציה למציאת הגורם הראשוני המינימלי של מספר שלם
# המספר הראשון שמתחלק במספר של הקלט, לא כולל המספר אחד

def smallest_factory(number):
    k=2
    while k <= number:
        if number%k == 0:
            print(k,"Is the smallest factory for the number",number)
            return k
        else:
            k = k + 1