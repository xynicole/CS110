'''
Xinyi Huang 
xhuang78@binghamton.edu
Jia Yang B58
Assignment11
'''

from libraryModule import StringGeneratorForDictionaries

'''
This class represents a library with books and patrons.
'''

class Library(object):

  ZERO = 0
#-- Class Variables ----------------------------------------------------

  # index when book not in library
  NOT_IN_LIBRARY = 0

  # index when book added to library
  ADD = 1

  # index when book removed from library
  REMOVE = 2

  # index when patron not a member of library
  NOT_A_MEMBER = 3

  # index when patron becomes member of library
  JOIN = 4

  # index when patron ends membership in library
  LEAVE = 5

  # index when book information is accessed
  ACCESS = 6

  # index when patron information is accessed
  LOOK_UP = 7

  # most reacent transaction with respect to either a book or a patron
  TRANS_STATUS = [" is not in library",
                  " has been added to the library",
                  " has been removed from the library ",
                  " is not a library member ",
                  " has been added as a library member",
                  " has been removed as a library member",
                  " has been accessed", 
                  " member files have been accessed"]
  
#-- Constructor --------------------------------------------------------

  # params:  name - name of Library(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__books (dict of Book)  and
  #              self.__patrons() (dict of Patron) to empty dictionaries,
  #              self.__transaction_status (str) to TRANS_STATUS with respect to
  #                book participating in transaction or
  #                patron participating in transaction
  def __init__(self, name):
    self.__name = name
    self.__books = {}
    self.__patrons = {}
    self.__transaction_status = self.TRANS_STATUS[Library.ZERO]
    

#-- Accessors ----------------------------------------------------------

  def get_name(self):
    return self.__name    

  # returns:  record of latest transaction (str)
  def get_transaction_status(self):
    return self.__transaction_status   

  # params:  title of Book (str)
  # invokes:  in_library(), __set_transaction_status()
  # returns:  Book stored in library (Book) or None
  def get_book(self, title):
    if self.in_library(title):
      self.__set_transaction_status(title,"", Library.ACCESS)
    else:
      self.__set_transaction_status(title, "", Library.NOT_IN_LIBRARY)
    return self.__books.get(title)
    

  # params: name of Patron who is member of library (str)
  # invokes:  is_member(),  __set_transaction_status()
  # returns:  name of Patron (Patron) or None
  def get_patron(self, name):
    if self.is_member(name):
      self.__set_transaction_status("", name, Library.LOOK_UP)
    else:
      self.__set_transaction_status("", name, Library.NOT_A_MEMBER)
    return self.__patrons.get(name)

#-- Predicates ---------------------------------------------------------


  # params: title - title of Book to search for in library (str)
  # returns:  True if in library, False otherwise (bool)
  def in_library(self, title):
    return title in self.__books 

  # params: name - name of Patron to search for in library (str)
  # returns:  True if member of library, False otherwise (bool)
  def is_member(self, patron_name):
    return patron_name in self.__patrons  

  # invokes:  len()
  # returns:  True if library has any books, False otherwise (bool)
  def has_books(self):
    return len(self.__books) > Library.ZERO
  
  # invokes:  len()
  # returns:  True if library has any members, False otherwise (bool)
  def has_members(self):
    return len(self.__patrons) > Library.ZERO

#-- Mutators -----------------------------------------------------------
    
  # params:  title - title of Book participating in transaction (str)
  #          name = name of Patron participating in transaction (str)
  #          Note:  one of the above should be an empty string
  #          index into TRANS_STATUS (int)
  def __set_transaction_status(self, title, name, index):
    self.__transaction_status = title + name + Library.TRANS_STATUS[index]

  # params:  book - new Book to be added to library (Book)
  # invokes:  get_title() (_book), __set_transaction_status()
  def add_book(self, book):
    self.__books[book.get_title()] = book
    self.__set_transaction_status(book.get_title(),"", Library.ADD)

  # params:  title - title of Book to remove from library (str)
  # invokes:  pop() (list),
  #           is_checked_out() (_book), get_patron (Book)
  #           decrement () (Patron)
  #           in_library(), __set_transaction_status()
  def remove_book(self, title):
    if self.in_library(title):
      val_book =self.__books.pop(title)
      if val_book.is_checked_out():
        val_book.get_patron().decrement()
      self.__set_transaction_status(title, "", Library.REMOVE)

    else:
      self.__set_transaction_status(title, "", Library.NOT_IN_LIBRARY)
      

  # params:  patron - new Patron to add to library (Patron)
  # invokes:  get_name (Patron), __set_transaction_status()
  def add_patron(self, patron):
   self.__patrons[patron.get_name()] = patron
   self.__set_transaction_status("", patron.get_name(), Library.JOIN)

  # params:  name - name of Patron to remove from library (str)  
  # invokes:  pop() (list),
  #           has_checked_out_books() (Patron) 
  #           get_patron (Book), return_me (Book)
  #           is_member(), __set_transaction_status()
  def remove_patron(self, name):
    if self.is_member(name):
      val_patron = self.__patrons.pop(name)
      if val_patron.has_checked_out_books():
        for book_key in self.__books.keys():
          if self.__books[book_key].get_patron() == val_patron:
             self.__books[book_key].return_me()
      self.__set_transaction_status("", name, Library.LEAVE)
    else:
      self.__set_transaction_status("", name, Library.NOT_A_MEMBER)
          
    

#-- Convert to Str -----------------------------------------------------

 # creates:  StringGeneratorForDictionaries objects
  # invokes:  str(), get_name(), has_books(), has_members(),
  #           get_dict_string() (StringGeneratorForDictionaries)
  # returns:  str representation of Library object (str)  
  def __str__(self):
    dict_book = StringGeneratorForDictionaries(self.__books, "Books")
    dict_patr = StringGeneratorForDictionaries(self.__patrons, "Patrons")
    if not self.has_books() or not self.has_members():
      string = "\n%s\n" % self.get_name()
      if not self.has_books():
        par_one = string + "There are no books in the library\n"
      else:
        par_one = string + dict_book.get_dict_string()
      if not self.has_members():
        libr_one = "There are no patrons in the library\n" + par_one
      else:
        libr_one = dict_patr.get_dict_string() + par_one
    else:
      libr_one = dict_book.get_dict_string() +dict_patr.get_dict_string()
    return libr_one
        
  
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
