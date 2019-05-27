import tkinter
import tkinter.messagebox

'''
Demonstrates Tk class destroy() method when Quit button clicked
as well as info dialog box
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__main_window = tkinter.Tk()

    # Create button with 'Click Me!' on face
    # doSomething method executed when clicked
    self.__my_button = tkinter.Button(self.__main_window, \
                                    text='Click Me!', \
                                    command=self.do_something)

    # Create Quit button that executes root widget's destroy() method
    # when clicked
    self.__quit_button = tkinter.Button(self.__main_window, \
                                      text='Quit', \
                                      command=self.__main_window.destroy)

    # Pack the Buttons
    self.__my_button.pack()
    self.__quit_button.pack()
    
    # Start listener
    tkinter.mainloop()

  # Event handler aka callback function for button   
  def do_something(self):
    # Display info dialog box
    tkinter.messagebox.showinfo('Response', \
                                'Thanks for clicking the button.')

MyGUI()

