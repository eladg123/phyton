start=10000
spend_list=[1200,900,354,1300,550,620,550,715]

total = sum(spend_list)

print("Total:",total)

money_left = start-total

print("Money left:",money_left)

average = total/len(spend_list)

print("The average per week:",average)

weeks_left = money_left/average

print('You have approx',weeks_left, "weeks left to travel.")