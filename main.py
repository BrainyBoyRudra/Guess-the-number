import random
number = random.randint(1,100)
name = input('What is your name ? ')
print('Hi',name ,'Guess any number between 1 to 100 ')
numberofguesses = 0
while numberofguesses < 5 :
    guess = int(input())
    numberofguesses += 1
    if guess < number :
        print('Your Guess is low')
    elif guess > number :
        print('Your Guess is High')
    else :
        break
if guess == number :
    print('Hurray! You have Guessed the number! in ' + str(numberofguesses) + ' guesses')
else :
    print('Your Guesses were wrong the correct number is ' + str(number)+ '.')