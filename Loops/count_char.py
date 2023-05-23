def count_char(s, c):
    counter = 0
    for char in s:
        if char == c:
            counter = counter+1
    return counter


# count how much c in the string s