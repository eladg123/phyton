temp = 25
is_raining = True

hat = False
umbrella = False 
coat = False

if temp > 15:
 hat = True
 coat = False
else: 
 hat = False
 coat = True

if is_raining == True:
 umbrella = True
else:
 umbrella = False

if hat:
 print('You should take a hat')
else:
 print("You should not take a hat")

if coat:
 print("You should take a coat")
else:
 print('You should not take a coat')

if umbrella:
 print('You should take an umbrella')
else:
 print("You should not take an umbrella")