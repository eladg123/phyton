def all_pairs_sum(num1,num2):
    sum = 0
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            sum = sum + i*j
    return sum


print(all_pairs_sum(3,4))