# כל זוגות המספרים מ1 עד n
def all_pairs(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("i =",i,"j =",j)


all_pairs(3)