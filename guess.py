
guess = 0
tries =  0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries +1
  print(f"number of times gone. {tries}")
  
  if guess == 6:
        print("You got it!")
  elif tries < 5:
        print('you have a few more tries')
  else:
       print("Your out of tires!")



