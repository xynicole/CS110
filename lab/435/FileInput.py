READ_MODE = 'r'

def main():
  print("This program will read in and print the contents of a file\n")
  fileName = input("Input a filename:  ")

  try: # outer try for infile open
    inFileObject = open(fileName, READ_MODE)

    try: # inner try for processing infile
      contents = inFileObject.readlines()
      for line in contents:
        print(line[:-1])

    except IOError as err: # inner exception handler for infile processing
      print("\nProblem reading data: \n" + str(err))
    except ValueError as err:# inner exception handler for infile processing
      print("\nProblem processing data, wrong format or corrupted? \n" + str(err) + '\n')
    except Exception as err: # inner exception handler for infile processing
      print("\nData cannot be read:  \n" + str(err) + '\n')
    finally: # will close file whether or not exception has been raised
      inFileObject.close()
      
  except FileNotFoundError as err:  # outer exception handler for infile open
    print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
  except IOError as err: # outer exception handler for infile open
    print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')


main()
