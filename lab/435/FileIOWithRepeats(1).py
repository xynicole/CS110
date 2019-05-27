READ_MODE = 'r'
WRITE_MODE = 'w'

def makeName(fileName):
  fileNameList = fileName.split('.')
  fileNameList[0] += "Output"
  return '.'.join(fileNameList)

def main():
  print("This program will read in the contents of a file, " +
        "then print and write the contents to a new file\n")
  fileName = input("Input a filename:  ")
  while fileName:




    #########################################
    #                                       #
    # PUT YOUR FIRST VALIDATION LOOP HERE,  #
    # FOLLOWED BY GETTING AND VALIDATING    #
    # THE REST OF YOUR INPUT, ONE AFTER     #
    # THE OTHER IN A BLOCK.                 #
    # ALL OF THE NON-VALIDATION ASSIGNMENT  #
    # STATEMENTS USED TO GET YOUR INPUTS,   #
    # AS WELL AS THE HEADER OF YOUR ERROR   #
    # TRAPS, SHOULD BE AT THE SAME LEVEL    #
    # OF INDENTATION.                       #
    # YOU DON'T NEED EXCEPTION-HANDLING     #
    # HERE, YOUR ORIGINAL CODE WILL BE THE  #
    # SAME, DON'T CHANGE IT!                #
    #                                       #
    #########################################

    ###########################################
    #                                         #
    # ONCE YOU GET PAST GETTING THE KEYBOARD  #
    # INPUTS, START YOUR FILE PROCESSING      #
    # HERE'S WHERE YOUR EXCEPTION-HANDLING    #
    # GOES!                                   #
    #                                         #
    ###########################################

    
    try: # outer try for infile open
      inFileObject = open(fileName, READ_MODE)
##      print(inFileObject)

      try: # inner try for processing infile
        contents = inFileObject.readlines()
##        print(contents)

        ##################################################
        #                                                #
        #  THIS IS WHERE YOU WOULD PROCESS THE CONTENTS  #
        #  OF THE INPUT FILE AND PREPARE YOUR OUTPUT     #
        #                                                #
        ##################################################
       

        try:  # "outer" try for outfile open
          outFileObject = open(makeName(fileName), WRITE_MODE)

          try: # inner try to outfile processing
            for line in contents:

              outFileObject.write(line)          
##              print(line)

          except IOError as err: # inner exception handler for outfile processing
            print("\nProblem writing data: \n" + str(err))
          except ValueError as err:  # inner exception handler for outfile processing
            print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
          except Exception as err: # inner exception handler for outfile processing
            print("\nData cannot be written to file: \n" + str(err) + '\n')
          finally:# will close file whether or not exception has been raised
            outFileObject.close()

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
        inFileObject.close()
        
    except FileNotFoundError as err:  # outer exception handler for infile open
      print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
    except IOError as err: # outer exception handler for infile open
      print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')
    except Exception as err: # outer exception handler for infile open
      print("\nData cannot be read:  \n" + str(err) + '\n')

      
    fileName = input("Input a filename:  ")

main()
