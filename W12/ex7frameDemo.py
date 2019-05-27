import tkinter

'''
Creates labels in two different frames
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__main_window = tkinter.Tk()

    # Create two frames, for top and bottom of window
    self.__top_frame = tkinter.Frame(self.__main_window)
    self.__bottom_frame = tkinter.Frame(self.__main_window)

    # Create three labels that live in the top frame
    self.__label1 = tkinter.Label(self.__top_frame, \
                                text='Omne')
    self.__label2 = tkinter.Label(self.__top_frame, \
                                text='Trium')
    self.__label3 = tkinter.Label(self.__top_frame, \
                                text='Perfectum')
    
    # Pack the labels into the top frame so they are stacked
    # Note that this is the default behavior
    # (They would do this anyway)
    self.__label1.pack(side='top')
    self.__label2.pack(side='top')
    self.__label3.pack(side='top')
##    self.label1.pack()#side='top')
##    self.label2.pack()#side='top')
##    self.label3.pack()#side='top')

    # Create three labels that live in the bottom frame
    self.__label4 = tkinter.Label(self.__bottom_frame, \
                                text='Omne')
    self.__label5 = tkinter.Label(self.__bottom_frame, \
                                text='Trium')
    self.__label6 = tkinter.Label(self.__bottom_frame, \
                                text='Perfectum')
    
    # Pack the labels into the bottom frame so they are
    # arranged horizontally from left to right
    self.__label4.pack(side='left')
    self.__label5.pack(side='left')
    self.__label6.pack(side='left')
    
    # Then pack the frames into the main window
    self.__top_frame.pack()
    self.__bottom_frame.pack()

    # Start the listener
    tkinter.mainloop()

MyGUI()

