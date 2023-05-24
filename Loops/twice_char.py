# קוד שבודק אם יש תו שחוזר פעמיים ברצף במחרוזת כלשהי
def twice(st):
    # delete pass and fill in your code below
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            return True
    return False