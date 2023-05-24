def strings_friends(s1,s2):
    for c in s1:
        if c in s2:
            return True
    return False


# בודק אם לשני סטרינגים יש לפחות תו אחד משותף