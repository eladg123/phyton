# בודק האם הסטרינג שקיבלנו הוא מספר חיובי מסוג int
def is_positive_int(st):
    result = False
    if len(st) == 0:
        return False
    if not st[0]  in "123456789":
        return False
    for i in range(1, len(st)):
        if not st[i] in "0123456789":
            result =  True
     
   
      

