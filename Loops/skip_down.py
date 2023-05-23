def skip_down(num,skip):
    result = []
    while num >=0 :
        result.append(num)
        num = num - skip
    return result