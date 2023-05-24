# בדיקה אם ברשימה יש את האיבר איקס

def search(L,x):
    for e in L:
        if e == x:
            return True
    return False

# מחפש ברשימה את האיבר איקס אבל מהסוף של הרשימה
def search_reverse(L, x):
    for i in range(len(L)-1,-1,-1):
        print("i=",i,L[i])
        if x == L[i]:
            return True
    return False
    
    
print(search_reverse([1,2,3,4],1))

# חיפוש סדרתי
#חיפוש זה עובר על כל איברי הרשימה מההתחלה לסוף ובודק האם איקס נמצא באחד מהאיברים ברשימה