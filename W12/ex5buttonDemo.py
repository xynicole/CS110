from tkinter import *
#from tkinter import messagebox

'''
Demonstrates Button widget and info dialog box
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__main_window = Tk()

    # Create button with 'Click Me!' on face
    # doSomething method executed when clicked
    self.__my_button = Button(self.__main_window, \
                                    text='Click Me!', \
                                    command=self.do_something)

    # Pack the Button
    self.__my_button.pack()
    
    # Start the listener
    mainloop()

  # Event handler aka callback function for button   
  def do_something(self):
    # Display info dialog box
    messagebox.showinfo('Response', \
                        'Thanks for clicking the button.')

MyGUI()

