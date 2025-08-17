# Mini Game Project
# RPG Game where player chooses there actions

moves = ['Punch','Kick','Slash','Heal']



def player1(x):
   if x == 1:
      print(moves[0])
      player2(int(input('Player 2 Enter your move 1-4! ')))
   elif x == 2:
      print(moves[1])
      player2(int(input('Player 2 Enter your move 1-4! ')))
   elif x == 3:
      print(moves[2])
      player2(int(input('Player 2 Enter your move 1-4! ')))
   elif x == 4:
      print(moves[3])
      player2(int(input('Player 2 Enter your move 1-4! ')))
   else:
      print('Wrong Selection!')
      player1(int(input('Player 1 Enter your move 1-4! ')))

      

def player2(x):
   if x == 1:
      print(moves[0])
      player1(int(input('Player 1 Enter your move 1-4! ')))
   elif x == 2:
      print(moves[1])
      player2(int(input('Player 1 Enter your move 1-4! ')))
   elif x == 3:
      print(moves[2])
      player2(int(input('Player 1 Enter your move 1-4! ')))
   elif x == 4:
      print(moves[3])
      player2(int(input('Player 1 Enter your move 1-4! ')))
   else:
      print('Wrong Selection!')
      player2(int(input('Player 2 Enter your move 1-4! ')))



player1(int(input('Player 1 Enter your move 1-4! ')))

    