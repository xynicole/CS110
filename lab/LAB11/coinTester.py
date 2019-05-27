'''
Shows that encapsulation (i.e., data hiding)can be implemented by proper naming
Note:  Making data private (self.__ . . .) prevents direct access of instance
  data - forces user to use publice interface of class, i.e., accessor and
  mutator methods, etc.
Output:
  state of Coin object (str)
  value of Coin side_up (str)
Input:
  none (values generated randomly)
Uses:
  Coin class
'''

import coinPrivate  # to access the improved Coin class

# Create coin object and show how it is used
# Note that improper use has been prevented
def main():
  # Create an object from the Coin class.
  my_coin = coinPrivate.Coin()

  ok_str = "OK"
  while ok_str:

    # Display the side of the coin that is facing up.
    print (my_coin)

    # Toss the coin.
    print ('I am tossing the coin...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print()
    print("After tossing, display the side of the coin " + \
          "that is facing up.")
    print (my_coin)

    print()
    print("But now I'm going to try to cheat! \n" + \
          "I'm going to try to directly change \nthe value " + \
          "of the object's side_up attribute to 'Heads'.")
    my_coin.__side_up = 'Heads'

    # Display the side of the coin that is facing up.
    print (my_coin)

    print()
    print("I'm going to try to cheat again! \n" + \
          "Now I'm going to try to directly change \nthe value " + \
          "of the object's side_up attribute to 'Tails'.")
    my_coin.__side_up = 'Tails'
    
    # Display the side of the coin that is facing up.
    print (my_coin)

    print()
    ok_str = input("Press any key to continue, \n" + \
                      "press <Enter> to quit:  ")
    
# Call the main function.
main()
