from book import *
from patron import *
#from book_student_version import *
#from patron_student_version import *
from libraryModule import DIVIDER

# This is a tester for the Book class
# Note that it uses the Patron and Book classes as well as
#   a global constant from the library_module file
def main():

  #  Create a couple of patrons:
  patron = Patron('first')
  patron2 = Patron('second')
  
#-----------------------------------------------------------------------

  # Create a book and exercise 'to_string', accessors, and predicates
  print("Step 1")
  print(DIVIDER + 'Book: \n')
  
  book = Book('Guide to CS110', 'Williams')
  print(book)
  print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
        '\nPatron: \n' + (str(book.get_patron()) if book.is_checked_out() else '\nNone') +
        '\n' + book.get_waitlist_str() +
        'Transaction Status: ' + book.get_transaction_status())
  print('\nChecked Out? ' + str(book.is_checked_out()) + \
        '\nReserved? ' + str(book.is_reserved()) + \
        '\nHas Book? ' + str(book.has_book(patron)) + \
        '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))

  # Have patrons take max number of books out,
  # and then have patrons try to borrow this book (exercises borrow_me()
  #  as well as the private methods that it calls)
  # Exercise 'to_string', accessors, and predicates after each
  print("\nStep 2")
  print('\Max out patrons')
  two_patrons = [patron, patron2]
  for patron in two_patrons:  # max out
    for i in range(Patron.MAX_BOOKS_OUT):
      patron.increment()

  print("\nStep 3")
  print('\nTry to borrow')
  for patron in two_patrons: # try to take out book
    book.borrow_me(patron)
    print()
    print(book)
    print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
          '\nPatron: ' + (str(book.get_patron()) if book.is_checked_out() else 'None') +
          '\n' + book.get_waitlist_str() +
          'Transaction Status: ' + book.get_transaction_status())
    print('\nChecked Out? ' + str(book.is_checked_out()) + \
          '\nReserved? ' + str(book.is_reserved()) + \
          '\nHas Book? ' + str(book.has_book(patron)) + \
          '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))

  # Have patrons return all books out,
  # and then have patrons try to borrow this book (exercises borrow_me()
  #  as well as the private methods that it calls)
  # Exercise 'to_string', accessors, and predicates after each
  print("\nStep 4")
  print('\nReturn books')
  for patron in two_patrons:
    for i in range(Patron.MAX_BOOKS_OUT):
      patron.decrement()

  print("\nStep 5")
  print('\nTry to borrow')
  for patron in two_patrons: # try again to take out book
    book.borrow_me(patron)
    print()
    print(book)
    print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
          '\nPatron: ' + (str(book.get_patron()) if book.is_checked_out() else 'None') +
          '\n' + book.get_waitlist_str() +
          'Transaction Status: ' + book.get_transaction_status())
    print('\nChecked Out? ' + str(book.is_checked_out()) + \
          '\nReserved? ' + str(book.is_reserved()) + \
          '\nHas Book? ' + str(book.has_book(patron)) + \
          '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))

  # Have patrons try to borrow book again (exercises borrow_me()
  #  as well as the private methods that it calls)
  # Exercise 'to_string', accessors, and predicates after each
  print("\nStep 6")
  print('\nTry to borrow again')
  for patron in two_patrons: # try again to take out book
    book.borrow_me(patron)
    print()
    print(book)
    print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
          '\nPatron: ' + (str(book.get_patron()) if book.is_checked_out() else '\nNone') +
          '\n' + book.get_waitlist_str() +
          'Transaction Status: ' + book.get_transaction_status())
    print('\nChecked Out? ' + str(book.is_checked_out()) + \
          '\nReserved? ' + str(book.is_reserved()) + \
          '\nHas Book? ' + str(book.has_book(patron)) + \
          '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))

  # Have patrons try to return book (exercises return_me()
  #  as well as the private methods that it calls)
  # Exercise 'to_string', accessors, and predicates after each
  print("\nStep 7")
  print('\nReturn book:')
  for patron in two_patrons: # return book
    book.return_me()
    print(book)
    print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
          '\nPatron: ' + (str(book.get_patron()) if book.is_checked_out() else '\nNone') +
          '\n' + book.get_waitlist_str() +
          'Transaction Status: ' + book.get_transaction_status())
    print('\nChecked Out? ' + str(book.is_checked_out()) + \
          '\nReserved? ' + str(book.is_reserved()) + \
          '\nHas Book? ' + str(book.has_book(patron)) + \
          '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))    


  # Have patrons try to return book again(exercises return_me()
  #  as well as the private methods that it calls)
  # Exercise 'to_string', accessors, and predicates after each
  print("\nStep 8")
  print('\nTry to return book again')
  for patron in two_patrons: # try again to return book
    book.return_me()
    print(book)
    print('\nTitle: ' + book.get_title() + '\nAuthor: ' + book.get_author() + \
          '\nPatron: ' + (str(book.get_patron()) if book.is_checked_out() else '\nNone') +
          '\n' + book.get_waitlist_str() +
          'Transaction Status: ' + book.get_transaction_status())
    print('\nChecked Out? ' + str(book.is_checked_out()) + \
          '\nReserved? ' + str(book.is_reserved()) + \
          '\nHas Book? ' + str(book.has_book(patron)) + \
          '\nIs in waitlist? '+ str(book.is_in_waitlist(patron2)))


  # Create list of patrons and have each one first try to take out this book,
  # and then have each one return it (exercises borrow_me(),and return_me()
  #  as well as the private methods that they call)
  # Exercise 'to_string', accessors, and predicates after each
  # Shows whether or not waiting list is being properly maintained
  print("\nStep 9")
  print('\nShow that wait list is managed properly')
  more_patrons = []
  more_patron_names = ['first','second','third', 'fourth', 'fifth', 'sixth']
  print('\nTry to lend out book:')
  for name in more_patron_names:
    more_patrons.append(Patron(name))
  for patron in more_patrons:
    book.borrow_me(patron)
    print(book.get_transaction_status())
    print(book)
  print("\nStep 10")
  print('\nReturn book:')
  for patron in more_patrons:
    book.return_me()
    print(book.get_transaction_status())
    print(book)

main()
