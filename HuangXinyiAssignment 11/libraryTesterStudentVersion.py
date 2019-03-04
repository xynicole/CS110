from patron import *
from book import *
from library import *
#from patronStudentVersion import *
#from bookStudentVersion import *
#from libraryStudentVersion import *
from libraryModule import *

# This is a tester for the Library class
# Note that it uses the Patron, Book, and Library classes as well as
#   the classes from the libraryModule file
def main():

  patrons = ['Able', 'Baker', 'Charlie', 'Delta', 'Echo']
  book_titles = ['Absolut Python', 'Dummies for Python', \
                'Evolving Python', 'Python for Profit', \
                'Python for Reptiles']
  authors = ['Anya', 'Dullest', 'Everest', 'Prospero', 'Nagini']
    
  print(DIVIDER + 'Library: \n')

  
  #  Create named library and display its initial state
  #  Exercises constructor and 'to string'
  library = Library('The Python Library')
  
  print(DIVIDER + 'Initial state:  \n' + str(library))
  
#-----------------------------------------------------------------------    
  #  Add patrons to library and exercise 'to String', get_patron() and
  #  get_transaction_status() accessors, and add_patron() mutator, as well
  #  as the private methods they call

  print(DIVIDER + 'Adding patrons:')
  for name in patrons:
    library.add_patron(Patron(name))
    print(library.get_transaction_status())
    print(str(library.get_patron(name)))
  print('\nAfter adding patrons:  \n' + str(library))

#-----------------------------------------------------------------------

  # Add books to library and exercise 'to String', get_book() and
  #  get_transaction_status() accessors, and add_book() mutator, as well
  #  as the private methods they call
  
  print(DIVIDER + 'Adding books:')
  for title_index in range(len(book_titles)):                     
    library.add_book(Book(book_titles[title_index], authors[title_index]))          
    print(library.get_transaction_status())
    print(str(library.get_book(book_titles[title_index])))
  print('\nAfter adding books:  \n' + str(library))
  
#-----------------------------------------------------------------------    

  #  Access and take out books from library to exercise 'to String',
  #  get_book(), get_patron(), and get_transaction_status() accessors, and
  #  add_book() mutator from Book, as well as the private methods called
  print(DIVIDER + 'Taking out books:')
  
  for i in range(Patron.MAX_BOOKS_OUT):
    print()
    book = library.get_book(book_titles[i])
    print(library.get_transaction_status())
    book.borrow_me(library.get_patron(patrons[0]))
    print(library.get_transaction_status())
    print(book.get_transaction_status())
    print()                                            
    print(library)
#-----------------------------------------------------------------------

  #  Access/take out books from library again, to exercise 'to String',
  #  get_book(), get_patron(), and get_transaction_status() accessors, and
  #  add_book() mutator from Book, as well as the private methods called
  
  print(DIVIDER + 'Taking out books again:')
  
  for i in range(len(book_titles)):
    print()
    book = library.get_book(book_titles[i])
    print(library.get_transaction_status())
    book.borrow_me(library.get_patron(patrons[i]))
    print(library.get_transaction_status())
    print(book.get_transaction_status())
    print()                                            
    print(library)
#-----------------------------------------------------------------------

  # Try taking out book that is not in library
  
  print(DIVIDER + 'Accessing non-existent book:')
  
  book = Book('Unknowable Python', 'The Unknown Coder')
  print(book)
  book = library.get_book('Unknowable Python')
  print(library.get_transaction_status())
#-----------------------------------------------------------------------

  # Try accessing patron who is not member of library
 
  print(DIVIDER + 'Accessing non-existent patron:')

  patron = Patron('The Unknown Library Member')
  print(patron)
  patron = library.get_patron('The Unknown Library Member')
  print(library.get_transaction_status())
  
#-----------------------------------------------------------------------

  # Show current state of library
  
  print(DIVIDER + 'Current state of library:')
  
  print(library)
#-----------------------------------------------------------------------

  # Remove patron
  
  print(DIVIDER + 'Remove patron:')    

  print(library.get_patron(patrons[-1]))
  library.remove_patron(patrons[-1])
  print(library.get_transaction_status())
  library.get_book(book_titles[-1]).get_transaction_status()
  print(library.get_patron(patrons[-1]))
  print(library.get_transaction_status())          
  print(library)
#-----------------------------------------------------------------------

  # Remove book
  
  print(DIVIDER + 'Remove book:')

  book = library.get_book(book_titles[-2])
  print(book)
  library.remove_book(book_titles[-2])
  print(library.get_transaction_status())
  print(library.get_book(book_titles[-2]))
  print(library.get_transaction_status())
  book.get_transaction_status()
  print(library)
#-----------------------------------------------------------------------

  # Return books that are in library and have been taken out
  
  print(DIVIDER + 'Return books:')

  for title in book_titles:
    print()
    book = library.get_book(title)
    print(library.get_transaction_status())
    if book:
      book.return_me()
      print(library.get_transaction_status())
      print(book.get_transaction_status())
      print()                                            
  print(library)

#-----------------------------------------------------------------------

  # Save library to file
  
  print(DIVIDER + 'Save library:')    

  library_file_name = input('Input the file name that will be ' +\
                           'used to store library records:  ')
  library_records = LibraryRecords(library_file_name)
  library_records.save(library)
#-----------------------------------------------------------------------    

  # Load library from file

  print(DIVIDER + 'Load library:')    

  library_file_name = input('Input the file name that was ' +\
                           'used to store library records:  ')
  library_records = LibraryRecords(library_file_name)
  library = library_records.load()
  print('\nLibrary loaded:  \n' + str(library))
#-----------------------------------------------------------------------

  # Load data and create new library
  # Add book to new library

  print(DIVIDER + 'Can we maintain more than one?')

  print('Start with original: ')
  library2 = library_records.load()
  print('\nLibrary2 loaded from library:  \n' + str(library2))
  another_book = Book('Cloud Atlas', 'Mitchell')
  library2.add_book(another_book)
  print('\nLibrary2 after book added:  \n' + str(library2))

#-----------------------------------------------------------------------

  # Save new library
  
  print(DIVIDER + 'Save library2:')    

  library2_file_name = input('Input the file name that will be ' +\
                           'used to store library records:  ')
  library2_records = LibraryRecords(library2_file_name)
  library2_records.save(library2)
#-----------------------------------------------------------------------    

  #  Load new library (show display all records including new book)

  print(DIVIDER + 'Load library2:')    

  library2_file_name = input('Input the file name that was ' +\
                           'used to store library records:  ')
  library2_records = LibraryRecords(library2_file_name)
  library2 = library2_records.load()
  print('\nLibrary 2loaded:  \n' + str(library2))

#-----------------------------------------------------------------------    

  #  Load old library and compare records (should display old records)

  print(DIVIDER + 'Compare to original:')    

  library_file_name = input('Input the file name that was ' +\
                           'used to store original library records:  ')
  library_records = LibraryRecords(library_file_name)
  library = library_records.load()
  print('\nOriginal Library loaded:  \n' + str(library))

       
main()
