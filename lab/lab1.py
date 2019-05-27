
'''
Rose Williams
rosew@binghamton.edu
B5_
Lab #1
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many of each type of coin they have and output the total 

OUTPUT to monitor:
  total_dollars (float) - total amount of change in dollars

INPUT from keyboard:
  quarter_count (int)
  dime_count (int)
  nickel_count (int)
  penny_count (int)

GIVENS: 
  QUARTER_VALUE (int) - 25
  DIME_VALUE (int) - 10
  NICKEL_VALUE (int) - 5
  PENNY_VALUE (int) - 1
  TO_DOLLAR (int) - 100
'''

# CONSTANTS 
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1
TO_DOLLAR = 100

# This program outputs the total amount of change that a user has in dollars
# given the count of each type of coin

def main():
  # Explain purpose of program to user
  print("This program will print out the total amount of change " +
        "you have in dollars when you provide a count of each type of coin")

  # Ask user for number of coins they have
  # Start with quarters, end with pennies
  # Note constraints: no dollar, half-dollar coins
  quarter_count_str = input("Please enter the number of quarters you have:  ")
  dime_count_str = input("Please enter the number of dimes you have:  ")
  nickel_count_str = input("Please enter the number of nickels you have:  ")
  penny_count_str = input("Please enter the number of pennies you have:  ")

  # Convert str data to int
  quarter_count = int(quarter_count_str)
  dime_count = int(dime_count_str)
  nickel_count = int(nickel_count_str)
  penny_count = int(penny_count_str)

  # Multiply the value of each type of coin by it's count and sum each result
  total_cents = (QUARTER * quarter_count) + (DIME * dime_count) + \
                (NICKEL * nickel_count) + (PENNY * penny_count)

  # Convert to dollars (float)
  total_dollars = total_cents / TO_DOLLAR

  # Display labeled and formatted output in dollars
  print("The total amount of change you have in dollars is $%.2f" % \
        total_dollars)
  
main()
