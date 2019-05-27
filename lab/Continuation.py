# LOOP EXAMPLES

# ----------------------------------------------------------------------
# CONTINUATION LOOP - string data

# This is a PRIMING READ
name = input("Please enter your name or press <Enter> to quit:  ")

#  This is a CONTINUATION LOOP
while name:   #  When user hits Enter, program will end

  
  # Your entire program is nested within the body of this loop

  # This is a CONTINUATION READ:
  #   it keeps the program going as long as user enters more info
  # Note that it is the SAME AS Priming Read, only indented
  name = input("Please enter your name or press <Enter> to quit:  ")

#-----------------------------------------------------------------------
# CONTINUATION LOOP - numeric data


# This is a PRIMING READ
age_str = input("Please enter your age or press <Enter> to quit:  ")

# This is a CONTINUATION LOOP
while age_str:   # When user hits Enter, program will end
  
  age = int(age_str) # Convert only AFTER entering loop
  
  # Your entire program is nested within the body of this loop

  # This is a CONTINUATION READ:
  #   It keeps the program going as long as user enters more info
  # Note that it is the SAME AS Priming Read, only indented
  age_str = input("Please enter your age or press <Enter> to quit:  ")


# ----------------------------------------------------------------------
# CONTINUATION LOOP - multiple inputs

# This is a PRIMING READ
name = input("Please enter your name or press <Enter> to quit:  ")

# This is a CONTINUATION LOOP
while name:   # when user hits Enter, program will end
  
  # Your entire program is nested within the body of this loop

  # Take in other inputs, one after the other, inside the body of the loop
  age_str = input("Please enter your age:  ")
  # Why would we do this in two steps instead of all at once??  See below!
  age = int(age_str) # convert to numeric data

  # This is a CONTINUATION READ:
  #   It keeps the program going as long as user enters more info
  # Note that it is the SAME AS Priming Read, only indented
  name = input("Please enter your name or press <Enter> to quit:  ")
  
# ----------------------------------------------------------------------
# VALIDATION LOOPS inside CONTINUATION LOOP with multiple inputs
# (If you comment out everything above, you can run this to see how it works)

# Predicate function for validation
# param pin_str (str) - 4 character alphabet string used for PIN
# return True when pin_str has length of 4 and contains only alpha chars
def pin_validated(pin_str):
  return len(pin_str) == 4 and pin_str.isalpha()

# Predicate function for validation
# param age_str (str) - age input by user
# return True when age_str is made up of only digits and
#   (when converted to an int) is greater than 0 and less than 123
def age_validated(age_str):
  return age_str.isdigit() and int(age_str) > 0 and int(age_str) < 123

def main():

  print("This is a PRIMING READ")
  name = input("Please enter your name or press <Enter> to quit:  ")

  print('''
    BEFORE WHILE
    This is a CONTINUATION LOOP
    When the user enters data, the program continues
    When the user hits <Enter>, the program ends
    ''')
  while name:
    print('''
      AFTER WHILE
      Your entire program is nested within the body of this loop
      
      Some string input, like name, can't really be validated since people
        can make it whatever they want

      Now take in other inputs, one after the other, inside the body of the loop

      If a string has to follow a certain pattern, then it can be validated:
      ''')
    pin = input("Please enter your 4-character alphabetic PIN:  ")
    while not pin_validated(pin):
      print("You did not enter 4 alphabetic characters, please try again!")
      pin = input("Please enter your 4-character alphabetic PIN:  ")

    age_str = input("Please enter your age:  ")
    
    print('''
      Validate numeric input BEFORE converting to int or float:
      ''')
    
    while not age_validated(age_str):
      print("you did not enter a valid age, please try again!")
      age_str = input("Please enter your age:  ")
      
    print("Once validated, the string version can be converted to an int")
    
    age = int(age_str) 

    print('''
      ONCE ALL THE INPUT HAS BEEN TAKEN IN AND VALIDATED,
        THE PROGRAM WOULD CONTINUE TO PROCESS THE INPUT AND PRODUCE OUTPUT


      AFTER PRODUCING THE OUTPUT FOR THIS SET OF DATA,
        THE PROGRAM WOULD PROMPT THE USER FOR THE FIRST PIECE OF DATA
        FOR THE NEXT PROGRAM RUN
      IF THE USER ENTERS VALID DATA, THE PROGRAM WILL PROCEED
        (AND GET THE REST OF THE INPUT, ETC.)
      IF THE USER HITS <ENTER>, THEN THE PROGRAM WILL TERMINATE

      
      This is a CONTINUATION READ:
        It keeps the program going as long as user enters more info
      Note that it is the SAME AS Priming Read, only indented
      ''')
    name = input("Please enter your name or press <Enter> to quit:  ")

  print("That's all, folks!")
  
main()

  
