'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #5(2)
'''
'''
RESTATEMENT:
this program is based on lucky sevens ask a user to input a money value

OURPUT to monitor:
rolls number
money
value

INPUT to keyboard:
money


'''

import random

#CONSTANTS
SEVEN = 7
FOUR = 4
ONE = 1


# validation loop
def invalidMoney(money_str):
  return money_str.isdigit() and int(money_str) > 0


#put function to excute the game runs
def game(money):
  roll = 0
  high_money = 0
  high_roll = 0

  while money > 0:
    dice1 = random.randrange(1, SEVEN)
    dice2 = random.randrange(1, SEVEN)

    sum_dice = dice1 + dice2

    if sum_dice == 7:
      money = money + FOUR
    else:
      money = money - ONE

    roll += 1
    
    if money > high_money:
      high_money = money
      high_roll = roll
      
    print(roll, '\t', sum_dice, '\t', money)       

  return roll, high_roll, high_money 
    




  
def main():
  print("This is the game of Lucky Sevens.")
  money_str = input(
  "Please palce your bet in positive whole dollars OR press <Enter> to quit:  ")

#check the validate input
  while money_str:
    money = money_str

    while not invalidMoney(money_str):
      print("Invalid Input: Input whole numvers greater than 0 ONLY")
      money_str = input(
"Please palce your bet in positive whole dollars OR press <Enter> to quit:  ")
      money = money_str
  
    break
  money = int(money_str)


# create the table
  print("Roll",'\t',"Value",'\t',"Dollars")
  

  while money_str:

    roll, high_roll, high_money =game(money)
    break

  print("You become broke after: ",roll,"rolls")
  print("You should have quit after: ", high_roll,"\
rolls when you had $", high_money)

  money_str = input(
  "Please palce your bet in positive whole dollars OR press <Enter> to quit:  ")
  money= int(money_str)
  
main()
  
  


