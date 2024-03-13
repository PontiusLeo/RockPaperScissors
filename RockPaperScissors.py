import random
comput = random.randint(1,3)
if comput == 1:
    comput = "rock"
elif comput == 2:
    comput = "paper"
elif comput == 3:
    comput = "scissors"
player = ''
while (player != 'rock' and
       player != 'paper' and 
       player != 'scissors'):
    player = input("Make your choice: ")
while player == comput:
    player = input("Chose again, that was tie: ")    
#if comput == "rock" and player == 'rock':
    #print("That\'s the first tie, we play again")
if comput == 'rock' and player == 'paper':
    print("Congratualtions. Your paper covers my Rock. You win")
elif comput == 'rock' and player == 'scissors':
    print("Boo!!. take the middle finger. My Rock blunts your Scissors. You lose. You suck")
elif comput == 'paper' and player == 'rock':
    print("My paper wraps your Rock. I win. You lose")
#elif comput == 'paper'and player == 'paper':
 #   print("That\'s a second tie. We play again")
elif comput == 'paper' and player == 'scissors':
    print("Good job there. Your Scissors has cut my Paper. You win")
elif comput == 'scissors' and player == 'rock':
    print("You win. Your Rock has bluntened my Scissors")
elif comput == 'scissors' and player == 'paper':
    print("I win, sucker. My scissors cuts your paper. Go home and cry")
#elif comput == 'scissors' and player == 'scissors':
  #  print("That\'s third tie. We play again")
else:
    print("Wrong choice, choose Rock, Paper, or Scissors")