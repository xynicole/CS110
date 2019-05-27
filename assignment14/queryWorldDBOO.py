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
import os
import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Invalid Arguement'
    self.__message = 'Population is not digit'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def get_title(self):
    return self.__title

    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDB:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, db_name):
    conn = sqlite3.connect(db_name)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
    self.__current_city = ""



# -- Mutators ----------------------------------------------------------------

  # 
  # param city_name (str)
  def set_city(self, city_name):
    self.__current_city = city_name


  # raises BadArgument Exception if city is blank or contains invalid chars
  def pop_query(self):
    if self.__current_city.replace('_','A').isalpha():
      self.__cursor.execute('select population from city where name = ?',\
                          (self.__current_city,))
    else:
      raise BadArgument()

  def set_answer(self,min_pop,max_pop,cursor):
    self.__cursor.execute("select name, population from city where population"\
                   "< ? and population > ? order by population desc" ,(max_pop,min_pop))
    #cities = cursor.fetchall()
    #return cities


  # Close connection to db
  def close_connection(self):
    self.__cursor.close()

# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that if city isn't in database, then answer will be None
    # If city is in database, answer will be a tuple object
    # Will have to get element[0] of tuple in order to use it
    answer = self.__cursor.fetchall()
    ##print(answer)

    # Note that 4th format specifier denotes a string rather than an int in 
    # order to accommodate possibility that answer is None
    return_string = ''
    for data in answer:
      return_string += 'City: %s Pop: %s\n' % (data[0],data[1])
    return return_string
    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
  
# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def is_valid_range(min_pop, max_pop):
    return min_pop.isdigit() and max_pop.isdigit() and\
           max_pop >= min_pop

  
def main():
  min_pop = None
  max_pop = None
  path = os.getcwd() + "/worldDB"
  conn = sqlite3.connect(path)
  cursor = conn.cursor()
  query = QueryWorldDB('worldDB')
  #query = QueryWorldDB('world.db')

  # get input from user (priming read)
  max_pop = input("Enter max population:  ")
  min_pop = input("Enter min populaiton:  ")
  
  # let user get as many results as desired
  while max_pop and min_pop:
    try:
      # set up and issue query
      is_valid_range(min_pop,max_pop)
      
      # show results
      query.set_answer(min_pop,max_pop,cursor)                                                           
      print(query)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.get_title(), str(err) ))
       
    # let user enter another city (continuation read)
    max_pop = input("Enter max population:  ")
    min_pop = input("Enter min populaiton:  ")
    
  # close connection to db
  query.close_connection()

main()
                            
                            
                    
