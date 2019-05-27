READ_MODE = 'r'

def main():
  print("This program will read in and print the contents of a file\n")
  fileName = input("Input a filename:  ")
  inFileObject = open(fileName, READ_MODE)
  contents = inFileObject.readlines()
  for line in contents:
    print(line[:-1])
  inFileObject.close()
      
main()
