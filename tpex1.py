secret=7
num=int(input("enter your guess: "))
while num!=secret:
    if num>secret:
     num=int(input("too high, try again: "))
    elif num<secret:
      num=int(input("too low, try again: "))
print("Congratulations! You've guessed it.")