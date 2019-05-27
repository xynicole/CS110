import tkinter

'''
Displays a label with text
'''
class MyGUI:
  def __init__(self):
    # Create tmain window
    self.__main_window = tkinter.Tk()

    # Create Label and set its text field
    self.__label = tkinter.Label(self.__main_window, \
                               text='Hello World!')

    # Call the Label widget's pack method
    self.__label.pack()

    # Start listener
    tkinter.mainloop()

MyGUI()

