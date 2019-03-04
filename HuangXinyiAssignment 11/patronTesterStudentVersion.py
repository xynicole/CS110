from patron import *
#from patron_student_version import *
from libraryModule import DIVIDER

# This is a tester for the Patron class
# Note that it uses the Patron class as well as the global constant 
#   from the library_module file
def main():
#-----------------------------------------------------------------------------
  # Create patron and exercise 'to string', accessors and predicates

  print(DIVIDER + 'Patron: \n')
  
  patron = Patron('first')
  print(patron)
  print('\nName: ' + patron.get_name() + 'Status: ' + patron.get_status() + \
        '\nBooks Out: ' + str(patron.get_num_books_out()))
  print('\nCan Take out Books? ' + str(patron.can_check_out_books()) + \
        '\nHas Books Checked Out? ' + str(patron.has_checked_out_books()))

  print()
  
  # Take out books until max amount have been taken out
  # Exercise 'to String', accessors, predicates, and increment() mutator
  # update_status() will be exercised automatically
  
  # Note:  Book controls whether or not this should be done
  for i in range(Patron.MAX_BOOKS_OUT):
    print('\nHave patron take book out:  ' + str(i + 1))
    patron.increment()
    print(patron)
    print('\nName: ' + patron.get_name() + '\nStatus: ' + patron.get_status() + \
          '\nBooks Out: ' + str(patron.get_num_books_out()))
    print('\nCan Take out Books? ' + str(patron.can_check_out_books()) + \
          '\nHas Books Checked Out? ' + str(patron.has_checked_out_books()))

  print()
  
  # Return books until all have been returned
  # Exercise 'to String', accessors, and decrement() mutator
  # update_status() will be exercised automatically
  
  for i in range(Patron.MAX_BOOKS_OUT):
    print('\nHave patron return books:  ' + str(i + 1))
    patron.decrement()
    print(patron)
    print('\nName: ' + patron.get_name() + '\nStatus: ' + patron.get_status() + \
        '\nBooks Out: ' + str(patron.get_num_books_out()))
    print('\nCan Take out Books? ' + str(patron.can_check_out_books()) + \
          '\nHas Books Checked Out? ' + str(patron.has_checked_out_books()))

main()  
