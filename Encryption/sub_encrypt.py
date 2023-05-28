import random
# צופן הצבה - יצירת סדר חדש של אותיות רנדומלי ומחליפים אות על פי מיקומה
def sub_encrypt(plaintext,alphabet,shuffeld):
    cipherText = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffeld[position]
            cipherText = cipherText + new_char
        else:
            cipherText = cipherText + char
    return cipherText


alphabet  = "abcdefghijklmnopqrstuvwxyz"
shuffled = "psfvinytdugqrjhwebmkzoxcla"




# פענוח צופן הצבה
def sub_decrypt(cipherText,alphabet,shuffled):
    plainText = sub_encrypt(cipherText,shuffled,alphabet)
    return plainText



cipherText= sub_encrypt("hello! world!",alphabet,shuffled)
print(cipherText)
plainText = sub_decrypt(cipherText,alphabet,shuffled)
print(plainText)


# how to shuffle alphabet:
# random.shuffle(alphabet)