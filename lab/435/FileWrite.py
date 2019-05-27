WRITE_MODE = 'w'

def main():
#  ''' #1
  print("This program will write the contents of a list to a file\n")
  fileList = \
    ['Captain Midnight and the Secret Squadron\n', '\n',
     'And now boys and girls, here is what you get when you join the Secret Squadron:  this\n',
     'membership card with your own secret squadron number, this official Secret Squadron manual, \n',
     "and this combination badge and decoder.  Look, here's how the decoder works:  \n",
     "I'll give you a two word clue, and the second word is in our secret code.\n",
     'The first word is "WATCH". Now, here is the secret code word - write down these numbers:  17-3-20!\n',
     'Now, set your secret decoder like this:  for CODE A-3.  Then decode this important clue to next \n',
     "week's adventure.  \n", '\n',
     "If you don't have your decoder badge, here's how you can get one for your very own.  First, get a jar \n",
     'of the official secret squadron drink:  delicious chocolate-flavored Ovaltine.  The food drink for rocket\n',
     'power!  Then cut out the wax paper disk that covers the Ovaltine jar, and send that disk with your name, \n',
     "your address to me, Captain Midnight Box P Chicago 77, Illinois.  That's all, send no money, it's free to \n",
     'every boy and girl who join the secret squadron.  And when you receive your secret decoder badge, membership\n',
     'card with your very own secret squadron number, and 12 page manual you will be a full-fledged member.  Remember,\n',
     "get your Ovaltine, the food drink for rocket power!  Hot or cold, it's got what it takes for you to be a leader \n",
     'in your gang!  So every day, drink instant Ovaltine!\n']
 
  fileName = "midnightCopy.txt"

  '''
  fileList = [1,2,3,4,5]
  fileName = "numbers.txt"
  ''' #2
  
  try:  # "outer" try for outfile open
    outFileObject = open(fileName, WRITE_MODE)

    try: # inner try for outfile processing
      for line in fileList:              
        outFileObject.write(line)

    except IOError as err: # inner exception handler for outfile processing
      print("\nData cannot be written to file: \n" + str(err) + '\n')
    except TypeError as err: # inner exception handler for outfile processing
      print("\nData cannot be written to file, wrong format, File corrupted? \n" + str(err) + '\n')
    finally: # will close file whether or not exception is thrown
      outFileObject.close()

  except IOError as err: # "outer" exception handler for outfile open
    print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')
        
main()
