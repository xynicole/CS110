'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #5 (3)
'''

'''
RESTATEMENT:
 computes the amount of money a person would earn over a period of time
 
INPUT:
num_days

OUTPUT to monitor:
  salary

FORMULA:
  salary = total_penny / HUNDRE
  total_penny = total_penny *TWO
'''




#CONSTANTS

EIGHT = 8
TWO = 2
ZERO = 0
ONE = 1
HUNDRED = 100

#purpose of this program

print(" computes the amount of money a person would earn over a period of \
time if his or her salary is one penny the first day, two pennies the second \
day, and continues to iuble each day.")

 
# validation loop

def invalidDay(num_days_str):
  return num_days_str.isdigit() and int(num_days_str) > 0


#put function to calculate the penny

def compute_penny(x):
  return TWO**(x - ONE)

def main():
  num_days_str = input("Enter the number of days worked:   ")
    

# while loop

  while num_days_str:
    num_days = num_days_str


    while not invalidDay(num_days_str):
       print("Days must be a positive value greater than zero")
       num_days_str = input("Enter the number of days worked:   ")
       num_days = num_days_str
    num_days = int(num_days_str)       
# table
    
    print("Day", '\t'*EIGHT,  "pay")
    print("---------" *EIGHT)



# for loop to compute days and salary

    penny = 0
    
    
    for i in range(1, num_days+1):
      my_penny = compute_penny(i)
      penny += my_penny
      print(i,'\t' *EIGHT, my_penny)
    salary = penny / HUNDRED
    print("Your salary on", num_days, "days" " would be $%.2f" % salary)
    num_days_str = input(
      "Enter the number of days worked OR <ENTER> to quit:  ")
 
main()
