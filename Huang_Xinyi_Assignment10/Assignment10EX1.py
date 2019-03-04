'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #10 (1)
'''
"""
This program is to encrypts or decrypts a message in a file given the
operation to perform and either the rotation key (when encrypting) or the
rotation key that was used to encrypt (in the case of decrypting).
Then a new file will be made and encrypts or decrypts a message will be writen
down on the file.

Output to monitor:
  out_file_object(file)

Input from keyboard:
  file_name(str)
  operation(str)
  rotation_key(int)

Tasks allocated to functions:
  operation_validated() -- check the validaity of the operation
  rotation_key_validated() -- check the validatiy of the ratation
  convert_rotation_key() -- conver the ratation to the int
  keep_in_bounds() -- keep the roation in bounds
  process_message() -- encrypts or decrypts the message in file
  file_name_validated() -- check the validatiy of the file name
  make_name() -- make the name of the new file
  write_to_file() -- write the message on the new file
"""    

import os.path

#Initialize constants ---------------------------------------------------------

OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127

# Allowable rotation key prefixes
KEY_PREFIX = "-"

# Required file extension
FILE_EXT = ".txt"

# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w'

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
  return rotation_key_str.isdigit() \
      or (rotation_key_str[0]== KEY_PREFIX and rotation_key_str[1:].isdigit())

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
    ##print(char)
    new_message += chr(keep_in_bounds(ord(char) + rotation_key))
    ##print(new_message)
  return new_message

# Checks that file exists and that extension is .txt
# param name (str) - file name
# invoke isFile() from module os.path and endswith()
# return True when valid, False otherwise (bool)
def file_name_validated(name):
  return os.path.isfile(name) and name.endswith(FILE_EXT)


# Generates output file name from input file name, 
# operation requested and rotation key
# param fileName (str) - input file name
# param operation (str)
# param rotationKey (int) - converted key
# invoke str.split(), str.replace() and str.join()
# return output file name (str)
def make_name(file_name, operation, rotation_key):
  nameList = file_name.split(".")
  nameList[0] = nameList[0].replace(OPERATIONS['e'][1], "")
  nameList[0] = nameList[0].replace(OPERATIONS['d'][1], "")
  nameList[0] += (OPERATIONS[operation][1] + str(rotation_key))
  return ".".join(nameList)

#Processes list of lines from input file list one line at a time
#param newlist (list)
#param rotationKey (int)
#invoke list.append()
#       processLine()
#return list of processed lines (list)
def process_message_list(new_list, rotation_key):
  list_two = []

  for line in new_list:
    list_two.append(process_message(line.rstrip(), rotation_key)+"\n")
  return list_two
  

#Students can do this in the main() instead
#Write each line in output list of file
#param file(type: _io.TextIOWrapper -i.e., it's a text file)
#param textList(list)
#return None
def write_to_file(out_file_object, text_list):
  for line in text_list:

   out_file_object.write(line)
  
  return None
                    
# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
 

  # Describe program                   
  print("This program encrypts or decrypts entire files at a time using a " \
         "Caesar cipher")
  # Priming read and repeat
  file_name = input("Input the name of a file to be processed" \
         "(or press <Enter> to quit):  ")

  while file_name:
    while not file_name_validated(file_name):
      file_name = input("That file name does not appear to be valid, "\
                        "please try again:")
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
    
    try: # outer try for infile open
      in_file_object = open(file_name, READ_MODE)
##      print(in_file_object)

      try: # inner try for processing infile
        contents = in_file_object.readlines()
##        print(contents)
        
        out_message = process_message_list(contents, rotation_key)

        try:  # "outer" try for outfile open
          out_file_object = open(make_name(file_name,op_str,rotation_key), WRITE_MODE)

          try: # inner try to outfile processing
##            for line in contents:
              write_to_file (out_file_object, out_message)
##              out_file_object.write(line)          
##              print(line)

          except IOError as err: # inner exception handler for outfile processing
            print("\nProblem writing data: \n" + str(err))
          except ValueError as err:  # inner exception handler for outfile processing
            print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
          except Exception as err: # inner exception handler for outfile processing
            print("\nData cannot be written to file: \n" + str(err) + '\n')
          finally:# will close file whether or not exception has been raised
            out_file_object.close()

        except IOError as err: # "outer" exception handler for outfile open
          print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')
        except Exception as err: # outer exception handler for outfile processing
          print("\nData cannot be read:  \n" + str(err) + '\n')  

      except IOError as err: # inner exception handler for infile processing
        print("\nProblem reading data: \n" + str(err))
      except ValueError as err: # inner exception handler for infile processing
        print("\nProblem processing data, wrong format or corrupted? \n" + str(err) + '\n')
      except Exception as err: # inner exception handler for infile processing
        print("\nData cannot be read:  \n" + str(err) + '\n')        
      finally:# will close file whether or not exception has been raised
        in_file_object.close()
        
    except FileNotFoundError as err:  # outer exception handler for infile open
      print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
    except IOError as err: # outer exception handler for infile open
      print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')
    except Exception as err: # outer exception handler for infile open
      print("\nData cannot be read:  \n" + str(err) + '\n')

    file_name = input("Input the name of a file to be processed" \
         "(or press <Enter> to quit):  ")

main()


