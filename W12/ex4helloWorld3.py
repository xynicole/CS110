import tkinter

'''
Demonstrates the side='left' pack() method argument 
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__main_window = tkinter.Tk()

    # Create two labels and set their text
    self.__label1 = tkinter.Label(self.__main_window, \
                                text='Hello World!')
    self.__label2 = tkinter.Label(self.__main_window, \
                     text='This is my GUI program.')

    # Call both Label widgets' pack method
    self.__label1.pack(side='left')
    self.__label2.pack(side='left')

    # Start the listener
    tkinter.mainloop()

myGui = MyGUI()

