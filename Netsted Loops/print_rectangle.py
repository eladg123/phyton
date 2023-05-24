# הדפסת מלבן בגובה ורוחב שמקבלים כקלט

def print_rectangle(height,width):
    for i in range(1,height+1):
        for i in range(1,width+1):
            print('#',end=" ")   # end = לא יורד שורה
            if i == width:
                print("")         # = יורד שורה רק שמסיים את הרוחב לשורה זו



print_rectangle(5,10)