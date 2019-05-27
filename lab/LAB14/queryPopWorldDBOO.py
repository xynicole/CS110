'''
Rose Williams
'''

'''
This program finds the population of a city via database query
Output:
  query result (str)
Input:
  city (str)
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Bad Argument'
    self.__message = 'Population range is invalid'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def getTitle(self):
    return self.__title
    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDBPopRange:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, dBName):
    conn = sqlite3.connect(dBName)
    self.__cursor = conn.cursor()
    # pop ranges are instance variables: accessible to all methods
    self.__popMin = '' 
    self.__popMax = ''
    self.__answer = None

# -- Predicates ---------------------------------------------------------------

  def isValidRange(self):
    return self.__popMin.isdigit() and self.__popMax.isdigit() and \
           int(self.__popMin) <= int(self.__popMax)
           
# -- Accessors ----------------------------------------------------------------

  # return answer (str)
  def getAnswer(self):
    return self.__answer

# -- Mutators -----------------------------------------------------------------

  # param popMin(str)
  def setPopMin(self, popMin):
    self.__popMin = popMin

  # param popMax(str)
  def setPopMax(self, popMax):
    self.__popMax = popMax

  # Note that if no matches in database, then answer will be None
  # If matches are in database, answer will be a tuple of tuples
  def setAnswer(self):
    self.__answer = self.__cursor.fetchall()


  # raises BadArgument Exception if population range is invalid
  def citiesInPopRange(self):
    if self.isValidRange():
      self.__cursor.execute(
        'select name, population from city where population >=  ? and population  <= ? ' +
        'order by population desc', (self.__popMin, self.__popMax))                          
    else:
      raise BadArgument()


  # Close connection to db
  def closeConnection(self):
    self.__cursor.close()

# -- toString -----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that if no matches in database, then answer will be None
    # If matches are in database, answer will be a tuple of tuples
    # Will have to get element[0] of each tuple in order to use answer
    answerStr = 'The cities having populations between %s and %s are: \n' % \
                (self.__popMin, self.__popMax)
    if self.__answer:
      for row in self.__answer:
        answerStr += '%40s, %10d\n' % (row[0].replace('_', ' '), row[1])
    return answerStr
  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
  
# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def main():
  # set up connection and create cursor
  query = QueryWorldDBPopRange('worldDB')
  #query = QueryWorldDBPopRange('world.db')

  # get input from user (priming read)
  minimumPop = input("Find the cities within a given population range\n" + \
               "Enter the minimum population for range:" + \
               "(Press <Enter> to quit):  ")
  
  # let user get as many results as desired
  while minimumPop:
    # get remaining input
    maximumPop = input("Enter the maximum population for range:  ")  
    try:
      # set up and issue query
      query.setPopMin(minimumPop.strip())
      query.setPopMax(maximumPop.strip())      
      query.citiesInPopRange()
      query.setAnswer()
      # show results
      print(query)
    except BadArgument as err:
      # range invalid
      print('\n%s: %s\n' % (err.getTitle(), str(err) ))
       
    # let user enter another city (continuation read)
    minimumPop = input("Find the cities within a given population range\n" + \
                 "Enter the minimum population for range:" + \
                 "(Press <Enter> to quit):  ")
    
  # close connection to db
  query.closeConnection()

main()
                            
                            
                    
