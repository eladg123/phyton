table = [ [6, 9, -18, 12, 21], 
          [5, 20, 0, 4, 16], 
          [-6, 5, -12, -6, -13]]

table_sum = 0
table_min = 0
table_max = 0
sorted_table = []

table_sum = sum(table[0]) + sum(table[1]) + sum(table[2])
table_min = min(min(table[0]),min(table[1]),min(table[2]))
table_max = max(max(table[0]),max(table[1]),max(table[2]))
list1 = sorted(table[0])
list2 = sorted(table[1])
list3 = sorted(table[2])
sorted_table = sorted(list1+list2+list3)