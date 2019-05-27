def main():
  print("This program will divide two numbers of your choosing for as long as you like\n")
  divisorStr = input("Input a divisor:  ")
  while divisorStr:
    dividendStr = input("Input a dividend:  ")
    try:
      divisor = int(divisorStr)
      dividend = int(dividendStr)

      print (dividend / divisor)
    except ZeroDivisionError:
      print("You cannot divide by zero\n")
    except ValueError:
      print("You must input a number\n")
    except Exception:
      print("Something happened\n")
    
    divisorStr = input("Input a divisor:  ")

main()
