'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #8 (1)
'''
"""
Write a program that repeatedly encrypts or decrypts a message given the
operation to perform and either the rotation key (when encrypting) or the
rotation key that was used to encrypt (in the case of decrypting)

Output to monitor:
  new_message (str)

Input from keyboard:
  message (str)
  operation (str) - 'E', 'e', 'D', or 'd'
  rotation_key(int)

Tasks allocated to functions:
  operation_validated() - simple Predicate function
  rotation_key_validated() - simple Predicate function
  convert_rotation_key()
  keep_in_bounds()
  process_message()
"""    


#Initialize constants ---------------------------------------------------------

OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}
NEG_ONE = -1
# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127

# Allowable rotation key prefixes
KEY_PREFIX = "-"

# Functions ------------------------------------------------------------------

# Check that requested operation is valid
# param op_str (str) - operation requested
# invoke len()
# invoke str.lower()
# return  True when valid, False otherwise (bool)
def operation_validated(op_str):
  return len(op_str)==1 and op_str.lower() in OPERATIONS

        # Check that rotation key is of form <digits> or -<digits>
# param rotation_key_str (str)
# invoke str.isdigit() 
# returns:  True when valid, False otherwise (bool)
def rotation_key_validated(rotation_key_str):
  return rotation_key_str[1:].isdigit() or rotation_key_str.isdigit()

# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotation_key_str (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convert_rotation_key(op, rotation_key_str):
  rotation_key = int(rotation_key_str)
  return rotation_key * OPERATIONS[op][0]
  


# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
def keep_in_bounds(ordinal):
  ascii_diff = PRINTABLE_ASCII_LIMIT - PRINTABLE_ASCII_MIN
  while ordinal >= PRINTABLE_ASCII_LIMIT:
    ordinal = ordinal - ascii_diff
  while ordinal < PRINTABLE_ASCII_MIN:
    ordinal = ordinal + ascii_diff
  return ordinal 

# Encrypt or decrypt message using rotation_key
# param message (str)
# param rotation_key (int)
# invoke keep_in_bounds() 
# return processed_message (str)
def process_message(message, rotation_key):
  new_message = ''
  for char in message:
    new_message += chr(keep_in_bounds(ord(char) + rotation_key))
  return new_message 


# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")

  # Priming read and repeat
  message = input("Input the message to be processed OR <Enter> to quit:  ")

  # Get remaining inputs, validate and convert as necessary  
  while message:
    op_str = input("Enter e for encrypt or d for decrypt:  ")
    op_str = op_str.lower()
    while not operation_validated(op_str):
      print("Invaild value, please try again")
      op_str = input("Enter e for encrypt or d for decrypt:  ")
      op_str = op_str.lower()
    rotation_key_str = input("Enter the rotation key:  ")
    while not rotation_key_validated(rotation_key_str):
      print("Invalid rotation key, please try again")
      rotation_key_str = input("Enter the rotation key:  ")
    rotation_key = convert_rotation_key(op_str, rotation_key_str) 

    
    # Encrypt or decrypt contents of message
    # Display result
    
    print("Your new message is: %s" %(process_message(message, rotation_key)))

       # Continuation read
    message = input("Input the message to be processed OR <Enter> to quit:  ")

main()
