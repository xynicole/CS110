'''
Xinyi Huang
xhuang78@binghamton.edu
Jia Yang B58
Assignment11
'''

'''
This class represents a book with a title, author, status,
a patron to whom the book is checked out, and a list
of patrons waiting for it
'''
class Book:

  # Class Constants ----------------------------------------------------------

  # index when book is first created (int)
  NONE = 0
  
  # index when book is loaned successfully (int)
  SUCCESSFUL = 1
  
  # index when patron is put on waiting list (int) 
  WAIT = 2
  
  # index when request for loan is unsuccessful (int)
  UNSUCCESSFUL = 3
  
  # index when book is returned (int)
  RETURNED = 4
  
  # index when request for loan is invalid (int)
  INVALID = 5
  
  TRANS_STATUS = [" No transactions yet",
                  " successfully checked out ",
                  " has been put on waiting list for ",
                  " must return books before taking out ",
                  " has returned ",
                  " has recorded an invalid transaction re:  "]

  # Constructor --------------------------------------------------------------

  # Creates a new book with the given title and author
  # params:  title (str) and author (str) of book
  # initialize:  self.__title (str) and self.__author (str) to value of
  #                 value of incoming parameters
  #               self.__transaction_status (str) to no transactions yet,
  #               self.__patron (_patron) & self.__waitlist (list of Patrons) 
  #                 to null/empty values
  def __init__(self, title, author):
    self.__title = title
    self.__author = author
    self.__transaction_status = Book.TRANS_STATUS[Book.NONE]
    self.__patron = None
    self.__waitlist =[]
    
  # Predicates ---------------------------------------------------------------

  # returns: True when book is already loaned out, False otherwise (bool)
  def is_checked_out(self):
    return bool(self.__patron)
  #self.__transaction_status == Book.TRANS_STATUS[Book.UNSUCCESSFUL]

  # invokes len()
  # returns: True if Patron(s) are waiting for book, False otherwise (bool)  
  def is_reserved(self):
    return len(self.__waitlist) > 0

  # params: patron - a particular patron (Patron)
  # returns: True when Patron has checked out book, False otherwise (bool)  
  def has_book(self, patron):
   return patron == self.__patron

  # params: patron - a particular patron (Patron)
  # returns: True when given Patron is on waiting list, False otherwise (bool)  
  def is_in_waitlist(self, patron):
    return patron in self.__waitlist

  # Both return and lend
  # returns: True when previous transaction is "returned" and 
  #          current transaction is "lend", False otherwise (bool)  
  def __needs_two_part_status(self):
    return Book.TRANS_STATUS[Book.RETURNED] in self.__transaction_status and \
           "\n" not in self.__transaction_status

  # Accessors ----------------------------------------------------------------

  # returns: title of book (str)
  def get_title(self):
    return self.__title    
 
  # returns: author of book (str)
  def get_author(self):
   return self.__author

  # returns: Patron who has checked out book (str)
  def get_patron(self):  
    return self.__patron

  # invokes: str()
  # returns: str representation of waiting list for book (str)
  def get_waitlist_str(self):
    waitlist = "Waitlist: \n"
    for patron in self.__waitlist:
      waitlist += (str(patron) + "\n")
    return waitlist

  # returns: record of latest book transaction (str)
  def get_transaction_status(self):
    return self.__transaction_status

 # Mutators ------------------------------------------------------------------

  # This method delegates all responsibilities to private methods of class
  # invokes: has_book(), is_in_waitlist(), can_check_out_books(), is_checked_out(),
  #          __lend_book(), __put_in_wait_list(), and __set_transaction_status()
  # params:  patron - patron trying to borrow book (Patron)
  def borrow_me(self, patron):
    if self.has_book(patron) or self.is_in_waitlist(patron):
      self.__set_transaction_status(patron.get_name(), Book.INVALID)
      
    elif patron.can_check_out_books() and not self.is_checked_out():
      self.__lend_book(patron)
      self.__set_transaction_status(patron.get_name(), Book.SUCCESSFUL)

    elif patron.can_check_out_books() and self.is_checked_out():
      self.__put_in_wait_list(patron)
      self.__set_transaction_status(patron.get_name(), Book.WAIT)

    elif not patron.can_check_out_books():
      self.__set_transaction_status(patron.get_name(), Book.UNSUCCESSFUL)
    

  # Return book: release current patron, try to lend to waiting patron  
  # This method delegates all responsibilities to private methods of class
  # invokes: is_checked_out(), is_reserved(), get_name(),
  #          __reset_patron,(), __lend_to_next_patron(), and
  #          __set_transaction_status()
  def return_me(self):
    if self.is_checked_out():
      self.__set_transaction_status(self.__patron.get_name(),Book.RETURNED)
      self.__reset_patron()
      if self.is_reserved():
        self.__lend_to_next_patron()
        

  # invokes: increment() (Patron class)
  # params: patron - Patron borrowing book (Patron)
  def __lend_book(self, patron): 
    patron.increment()
    self.__patron = patron

  # invokes: decrement() (Patron class)
  def __reset_patron(self): #patron mutator
    self.__patron.decrement()
    self.__patron = None
    
  # Lend book to waiting patron if eligible; if not, remove from wait List
  # invokes: is_checked_out(), is_reserved(),
  #          pop() (from list), borrow_me()
  def __lend_to_next_patron(self): # waitlist mutator
    """lend book to waiting patron if eligible
    if not, remove from wait List"""  
    while not self.is_checked_out() and self.is_reserved():
      self.borrow_me(self.__waitlist.pop(0))

  # params:  patron - Patron to put in waiting list (Patron)
  # invokes: append() (to list)
  def __put_in_wait_list(self, patron): # waitlist mutator
    """add patron to wait list"""
    self.__waitlist.append(patron)

  # Creates string describing latest transaction
  # Combines name of patron participation in transaction with
  #   status of most recent transaction and title of this book 
  # params: name - name of Patron participating in transaction (str)
  #         index - index of transaction in TRANS_STATUS (int)
  # invokes: __needs_two_part_status()
  def __set_transaction_status(self, name, index):# trans_status mutator
    if self.__needs_two_part_status():
      self.__transaction_status ="\n" + name +Book.TRANS_STATUS[index] +\
      self.get_title()

    else:
      self.__transaction_status = name + Book.TRANS_STATUS[index] +\
      self.get_title()

  # Comparators --------------------------------------------------------------

  # Already written for you:
  # Include these in order to sort Book objects


  # Shows how two Books can be compared with respect to the < relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when they are not same Book and other is Book object and
  #            title of this Book is lexicographically lower than title of
  #            other Book, False otherwise (bool)   
  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__title < other.__title

  # Shows how two Books can be compared with respect to the == relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when both are same Book or both are Book objects and
  #            title and author are equal, False otherwise (bool)
  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and self.__title == other.__title)
      


  # Convert to Str -----------------------------------------------------------

  # invokes:  str(), get_waitlist_str()
  # returns:  str representation of Book object (str)
  def __str__(self):
    if self.is_checked_out():
      book_str = "Title:%s\nAuthor%s\nChecked out:%s\n%s"%\
                (self.__title, self.__author, str(self.__patron),\
                    self.get_waitlist_str())
    else:
      book_str = "Title:%s\nAuthor:%s\n%s\n%s"%(self.__title,\
               self.__author, "Not checked out", self.get_waitlist_str())

    return book_str
    
            
