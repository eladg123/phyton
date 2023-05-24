# חיפוש בינארי בהנחה שהרשימה ממוינת מלמטה למעלה
def binary_search(L,x):
    left=0
    right=len(L)-1
    while left <= right:
        mid = (left+right)//2
        if x == L[mid]:
            return True
        else:
            if x<L[mid]:
                right = mid-1
            else:
                left = mid+1
    return False


lst = [3,4,5,6,20,24,27,29,30,31,55,100,102]
print(binary_search(lst,1))


# complexity: log2(n)+1 = מספר הפעמים שצריך לחלק את הרשימה לשתיים ועוד שלב אחד כדי לגלות שטווח החיפוש התרוקן
# חיפוש בינארי
# חיפוש זה פועל על פי חלוקה לחצי כל פעם אחרי השוואת המטרה לאמצע הסדרה