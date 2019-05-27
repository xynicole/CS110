import random

'''
Simulates a coin that can be flipped
'''

class Coin:
  
  # Initializes sideUp (str) to "Heads"
  # Stores list of outcomes since they are strings  
  def __init__(self):
    self.valueList = ['Tails', 'Heads']
    self.sideUp = self.valueList[1]

#------------------------------------------------------------------------------
# Accessors

  # returns value of sideUp (str)
  def getSideUp(self):
    return self.sideUp

#------------------------------------------------------------------------------
# Mutators

  # Randomly generated 0 = "Tails"
  # Randomly generated 1 = "Heads"
  def toss(self):
    self.sideUp = self.valueList[random.randint(0,1)]

  

'''
Shows that encapsulation (i.e., data hiding)can be violated by carelessly
  naming instance data
Note:  neglecting to make data private (self.__ . . .) allows instance data
  to be accessed directly, instead of through accessors
Output:
  state of Coin object (str)
  value of Coin sideUp (str)
Input:
  none (values generated randomly)
Uses:
  Coin class
'''

# Create coin object and show how it is used
# Note that improper use can't be prevented since
#   data isn't private
def main():
  # Create an object from the Coin class.
  myCoin = Coin()

  okStr = "OK"
  while okStr:
    # Display the side of the coin that is facing up.
    print("START RUN")
    print()
    print ('This side is up to start: ', myCoin.getSideUp())
    print()
    
    # Toss the coin.
    print ('I am tossing the coin...')
    myCoin.toss()

    print()
    print("After tossing, display the side of the coin " + \
          "that is facing up.")
    print ('This side is up: ', myCoin.getSideUp())

    print()
    print("But now I'm going to cheat! \n" + \
          "I'm going to directly change \nthe value " + \
          "of the object's sideUp attribute to 'Heads'.")
    myCoin.sideUp = 'Heads'

    # Display the side of the coin that is facing up.
    print()
    print ('Now, this side is up no matter what: ',
           myCoin.getSideUp())

    print()
    print("I'm going to cheat again! \n" + \
          "Now I'm going to directly change \nthe value " + \
          "of the object's sideUp attribute to 'Tails'.")
    myCoin.sideUp = 'Tails'
    
    # Display the side of the coin that is facing up.
    print()
    print ('Now, this side is up no matter what: ',
           myCoin.getSideUp())

    print()
    okStr = input("Press any key to continue, \n" + \
                  "press <Enter> to quit:  ")

# Call the main function.
main()
