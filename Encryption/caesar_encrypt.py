# פונקציה למימוש צופן קיסר
def caesar_encrypt(plaintext,offset):          # plaintext = what we want to encrypt, offset = the encrypt key (היסט)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + offset) % 26
            new_char = alphabet[new_position]
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char    
    return ciphertext


# פונקציה למימוש פענוח הצפנה של צופן קיסר
def caesar_decrypt(ciphertext,originalOffset):    #ההיסט כאן הוא ההיסט המקורי שאיתו מצפינים
    originalPlainText = caesar_encrypt(ciphertext,-originalOffset)
    return originalPlainText

# print(caesar_decrypt("Tyzj zj kyv tfiivtk rejnvi !",17))


# פונקציה לשבירת צופן קיסר
# הכוונה היא לעבור על כל ההיסטים האפשריים בשפה האנגלית 1-26 כי 0 לא מסיט את האות בכלל
def caesar_break(cipherText):
    for offset in range(1,26):
        maybe = caesar_decrypt(cipherText,offset)
        print(offset,"--->",maybe)


caesar_break("jxu gkuijyed ev mxujxuh q secfkjuh sqd jxyda yi de cehu ydjuhuijydw jxqd jxu gkuijyed ev mxujxuh q ikrcqhydu sqd imyc")