


def main():
    
  f = open("temp_conv.txt", "w")
  print("{0:>16}{1:10}".format("Fahrenheit", "\t Celsius"))


  for fahrenheit  in range(-300,213):
    celsius = (5/9) * (fahrenheit - 32)

    print ("%10.2f  \t %10.2f" % (fahrenheit, celsius))


    f.writelines("Farenheit: %10.2f \t Celsius: %10.2f\n" % (fahrenheit, celsius))
   
  f.close()

   
main()
