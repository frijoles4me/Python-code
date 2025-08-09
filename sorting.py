Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Duck')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    Gryffindor = Gryffindor +1
    Ravenclaw = Ravenclaw +1
elif answer == 2:
    Hufflepuff = Hufflepuff +1
    Slytherin = Slytherin +1
else:
    print('Wrong input')


print('Q2) When I’m dead, I want people to remember me as:' )
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer ==1:
    Hufflepuff = Hufflepuff +2
elif answer ==2:
    Slytherin = Slytherin +2
elif answer ==3:
    Ravenclaw = Ravenclaw +2
elif answer == 4:
    Gryffindor = Gryffindor +2
else:
    print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?' )
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer ==1:
    Slytherin = Slytherin +4
elif answer ==2:
    Hufflepuff = Hufflepuff +4
elif answer ==3:
    Ravenclaw = Ravenclaw +4
elif answer ==4:
    Gryffindor = Gryffindor +4
else:
    print('Wrong Input')

print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

most_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)   # We'll learn about the max() function in Chapter 6

if Gryffindor == most_points:
  print('🦁 Gryffindor!')
elif Ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif Hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')

