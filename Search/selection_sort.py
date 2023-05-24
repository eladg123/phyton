# מיון מערך שמגיע לא ממוין
def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)
    return sorted_L

#complexity = (n*(n+1))/2
# מיון בחירה
# על מנת למיין רשימה ניקח בכל פעם את המינימום/מקסימום שלה ונדחוף אותו לרשימה חדשה