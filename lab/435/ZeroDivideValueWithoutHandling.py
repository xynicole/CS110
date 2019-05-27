def main():
  print("This program will divide two numbers of your choosing for as long as you like\n")
  divisorStr = input("Input a divisor:  ")
  while divisorStr:
    dividendStr = input("Input a dividend:  ")
    divisor = int(divisorStr)
    dividend = int(dividendStr)
    print (dividend / divisor)
    divisorStr = input("Input a divisor:  ")

main()
