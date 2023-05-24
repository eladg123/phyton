# בודק אם כל המספרים במערך שנקלט זוגיים

def all_even(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 != 0 and lst[i] != 0:
            return False
    return True


print(all_even([2]))