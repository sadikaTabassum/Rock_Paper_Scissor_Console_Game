import random


scissor='''
   _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''

rock='''
               - - - - - -
            - - - - -  - - -
          -    -  -  -   -  -
         -   - -   -  - -  -  -
           - - - - - - - -- - 



'''



paper='''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'      
'''


game_images=[rock,scissor,paper]

print("Welcome to Rock, Paper, Scissors")


user_choice=int(input("What do you wanna choose? Type 0 for rock, 1 for paper or 2 for scissor"))
if user_choice>=0 and user_choice<=2:
    print("You chose:")
    print(game_images[user_choice])

computer_choice=random.randint(0,2)

print(f"Computer chose :")
print(game_images[computer_choice])


if user_choice>=3 or user_choice<0:

     print("You typed an invalid number.You Lose!")

elif user_choice==0 and computer_choice==2:

    print("You win")

elif computer_choice==0 and user_choice==2:
    print("You lose")

elif computer_choice>user_choice:
    print("You lose!")
elif user_choice>computer_choice:
    print("You win!")

elif computer_choice==user_choice:
     print("It's a draw!")

