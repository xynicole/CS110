'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #6(2)
'''

'''
RESTATEMENT:
  Display tax for single and married filers given set of incomes

OUTPUT to monitor:
  marital_status[status] (str)
  total_income[status][income] (float)
  tax (float)

GIVEN:
  marital_status (str) - ['single', 'married']
  total_income[status][income] (float):
    [[0,9075, 9076, 36900, 36901, 89350, 89351,
      186350, 186351, 405100, 405101, 406750, 406751],
     [0, 18150, 18151, 73800, 73801, 148850, 148851,
      226850, 226851,  405100, 405101, 457600, 457601]]
  Define constants below

FORMULA:
  tax = base tax amount for bracket
          + (tax rate for bracket * (total_income[status][income]
          - base total_income[status][income] level for bracket))
'''

# No MAGIC numbers!
# CONSTANTS

# base total_income[status][income] levels
# for single and married tax brackets
SINGLE_BRACKET0 = 0
SINGLE_BRACKET1 = 9075
SINGLE_BRACKET2 = 36900
SINGLE_BRACKET3 = 89350
SINGLE_BRACKET4 = 186350
SINGLE_BRACKET5 = 405100
SINGLE_BRACKET6 = 406750

MARRIED_BRACKET0 = 0
MARRIED_BRACKET1 = 18150
MARRIED_BRACKET2 = 73800
MARRIED_BRACKET3 = 148850 
MARRIED_BRACKET4 = 226850
MARRIED_BRACKET5 = 405100
MARRIED_BRACKET6 = 457600

# Define base tax amounts for single and married tax brackets
BASE_SIN_0 = 0
BASE_SIN_1 = 907.50
BASE_SIN_2 = 5081.50
BASE_SIN_3 = 18193.75
BASE_SIN_4 = 45353.75
BASE_SIN_5 = 117541.25
BASE_SIN_6 = 118118.75

BASE_MAR_0 = 0
BASE_MAR_1 = 1815.0
BASE_MAR_2 = 10162.5
BASE_MAR_3 = 28925.0
BASE_MAR_4 = 50765.0
BASE_MAR_5 = 109587.5
BASE_MAR_6 = 127962.5



# Define tax rate applied to total_income[status][income] over
# base total_income[status][income] of given tax bracket
RATE_0 = 0.10
RATE_1 = 0.15
RATE_2 = 0.25
RATE_3 = 0.28
RATE_4 = 0.33
RATE_5 = 0.35
RATE_6 = 0.396

# This progam displays the simple tax for single and married
# filers given a set of incomes












 
  # Define marital status and income data
marital_status = ['s', 'm']
total_income = [[SINGLE_BRACKET0,SINGLE_BRACKET1, SINGLE_BRACKET1 + 1,
                   SINGLE_BRACKET2, SINGLE_BRACKET2 + 1,
                   SINGLE_BRACKET3, SINGLE_BRACKET3 + 1,
                   SINGLE_BRACKET4, SINGLE_BRACKET4 + 1,
                   SINGLE_BRACKET5, SINGLE_BRACKET5 + 1,
                   SINGLE_BRACKET6, SINGLE_BRACKET6 + 1],
                  [MARRIED_BRACKET0, MARRIED_BRACKET1, MARRIED_BRACKET1 + 1,
                   MARRIED_BRACKET2, MARRIED_BRACKET2 + 1,
                   MARRIED_BRACKET3, MARRIED_BRACKET3 + 1,
                   MARRIED_BRACKET4, MARRIED_BRACKET4 + 1,
                   MARRIED_BRACKET5, MARRIED_BRACKET5 + 1,
                   MARRIED_BRACKET6, MARRIED_BRACKET6 + 1]]
#checks to see that it only contains "s" or "m"
def is_valid_status(status):
    return status.isalpha() and status == ("s") or status == ("m")
#checks to see that it only contains digits and is >0
def is_positive(total_income_str):
    return total_income_str.isdigit() and int(total_income_str) > 0


def compute_tax_for_braket(net_income, rate, base_tax):
    return base_tax +(rate * net_income)
  
def compute_tax(status,income):
      # Use nested and chained conditionals to compute tax
      
  if status == "s":
      if income > SINGLE_BRACKET6:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET6,RATE_6,BASE_SIN_6)
      elif income > SINGLE_BRACKET5:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET5,RATE_5,BASE_SIN_5) 
      elif income > SINGLE_BRACKET4:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET4,RATE_4,BASE_SIN_4)
      elif income > SINGLE_BRACKET3:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET3,RATE_3,BASE_SIN_3)
      elif income > SINGLE_BRACKET2:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET2,RATE_2,BASE_SIN_2)
      elif income >  SINGLE_BRACKET1:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET1,RATE_1,BASE_SIN_1)
      elif income > SINGLE_BRACKET0:
        tax = compute_tax_for_braket(income-SINGLE_BRACKET0,RATE_0,BASE_SIN_0)
      else:
        tax = 0
  elif status == "m":
      if income > MARRIED_BRACKET6:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET6,RATE_6,BASE_MAR_6)
      elif income > MARRIED_BRACKET5:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET5,RATE_5,BASE_MAR_5)
      elif income > MARRIED_BRACKET4:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET4,RATE_4,BASE_MAR_4)
      elif income > MARRIED_BRACKET3:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET3,RATE_3,BASE_MAR_3) 
      elif income > MARRIED_BRACKET2:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET2,RATE_2,BASE_MAR_2)
      elif income > MARRIED_BRACKET1:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET1,RATE_1,BASE_MAR_1)
      elif income > MARRIED_BRACKET0:
        tax = compute_tax_for_braket(income-MARRIED_BRACKET0,RATE_0,BASE_MAR_0)
      else:
        tax = 0
  return tax

def main():

   # Explain what program does
  print(
    "This program computes a simple tax table for single and married filers")


  # loop through single, then married categories
  for i in range(len(marital_status)):
    status = marital_status[i]
    # loop thru income brackets - will go through single first, then married
    for j in range(len(total_income[0])):
      income = total_income[i][j]
      tax = compute_tax(status,income)
      
      print("Tax for %7s filer, with income $%9.2f = $%9.2f" %
           (marital_status[i], total_income[i][j], tax))



  
  status = input('Enter your marital status("s" or "m" only) OR <ENTER> to quit   ')
  while status:
    while not is_valid_status(status):
      print('Invalid Input: input only "s" or "m"')
      status = input('Enter your marital status("s" or "m" only) OR <ENTER> to quit   ')
      
    total_income_str = input('Please enter your total income:   ')
    while not is_positive(total_income_str):
      print('Invalid Input: input only whole number greater than 0')
      total_income_str = input(
        'Please enter your total income rounded up to the nearest whole number:  ')

     
    income = int(total_income_str)

    tax = compute_tax(status,income)
    

     
    
    print("You have to pay $%9.2f" % (tax))
    status=input('Enter your marital status("s" or "m" only) OR <ENTER> to quit   ') 

    
main()
