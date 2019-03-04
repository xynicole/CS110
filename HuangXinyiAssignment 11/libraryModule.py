'''
Rose Williams
rosew@binghamton.edu
CS110
Assignment 11
'''

# This module contains useful collaborating classes for libraries
# See if you can figure out how they work!

import pickle

DIVIDER = '\n' + ('-' * 70) + '\n'  # useful string for output

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# This is a utility class that generates a string representaion of an 
# entire dictionary"""
class StringGeneratorForDictionaries(object):

  #-- Constructor ------------------------------------------------------------
  
  #  Creates new string generator for given dictionary with given label
  def __init__(self, dictionary, dictionary_label):

    self.__dictionary = dictionary # dictionary
    self.__dictionary_label = dictionary_label # title of dictionary
 
  #-- Accessors --------------------------------------------------------------

  # Returns a string representation of the dictionary,
  # basically a 'to string' for dictionaries
  def get_dict_string(self):
    d_list = list(self.__dictionary.values())
    d_list.sort()
    return '\n' + self.__dictionary_label + ':\n' + \
           ('\n'.join(map(str, d_list)))        
  
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    
# Binary file I/O class for libraries (Saves/loads BINARY NOT TEXT file)
class LibraryRecords(object):

  #-- Constructor ------------------------------------------------------------

  # Creates file I/O object for libraries
  # params:  file_name - name of physical file on storage media  
  def __init__(self, file_name):
    self.__file_name = file_name    # give it a .dat extension!

  #-- Accessors --------------------------------------------------------------

  # Loads library from file 
  # returns:  library that was stored in file
  def load(self):
    library_file_obj = open(self.__file_name, 'rb')
    library = pickle.load(library_file_obj)
    library_file_obj.close()
    return library

  #-- Mutators ---------------------------------------------------------------

  # Creates binary representation of library and stores in file
  # params:  library - entire library object 
  def save(self, library):
    library_file_obj = open(self.__file_name, 'wb')
    pickle.dump(library, library_file_obj)
    library_file_obj.close()
