'''
Stores value in kilometers
Retrieves value in kilometers or miles
Displays value in kilometers and miles
'''

class KiloToMiles:
  # Constructor
  def __init__(self, kilo = 0.0):
    self.__kilo = float(kilo)
    self.__KILO_TO_MILES = 0.6214 # Conversion constant

  # ---------------------------------------------------------------------------
  # Accessors

  # return kilometers (float)
  def get_kilo(self):
    return self.__kilo

  # return kilo converted to miles (float)
  def to_miles(self):
    return self.__kilo * self.__KILO_TO_MILES

  # ---------------------------------------------------------------------------
  # Mutators
  
  # param kilo (float)
  def set_kilo(self, kilo):
    self.__kilo = kilo

  # param kilo (float)
  def reset_kilo(self):
    self.__kilo = 0.0

  # ---------------------------------------------------------------------------
  # 'toString'
  def __str__(self):
    return "\n%.2f kilometers = %.2f miles" % (self.get_kilo(), self.to_miles())



'''
def main():
  k = KiloToMiles(10)
  k2 = KiloToMiles()
  k2.set_Kilo(20)
  print(k, k2)

main()
'''
