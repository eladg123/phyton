def is_general_palindrome(st):
    st = st.replace(" ","")
    st = st.replace(",","")
    st = st.replace('.',"")
    st = st.lower()
    l = 0
    r = len(st)-1
    while l<r:
        if st[l] != st[r]:
            return False
        l = l+1
        r = r+1
    return True
