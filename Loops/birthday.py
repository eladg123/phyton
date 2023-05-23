import random

days = [i for i in range(1,32)]
months = [i for i in range(1,13)]

def birthday(day, month):
    random_day = random.choice(days)
    random_month = random.choice(months)
    count_rolls = 1
    print(random_day,random_month)
    while random_day != day or random_month != month:
        count_rolls = count_rolls + 1
        random_day = random.choice(days)
        random_month = random.choice(months)
    return count_rolls


# פונקציה שבודקת כמה הגרלות עד שמגיעים לחודש ויום (תאריך לידה) בקלט שנכנס בצורה רנדומלית