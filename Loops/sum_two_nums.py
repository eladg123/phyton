# חישוב חיבור של שני מספרים

def sum_two_nums(num1,num2):
    res = num1
    while num1+num2 != res:
        res = res +1
    return res


def sum_two_nums_v2(num1,num2):
    res = num1
    for i in range(num2):
        print(i)
        res = res+1
    return res
