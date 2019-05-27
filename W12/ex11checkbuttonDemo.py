import tkinter
import tkinter.messagebox

'''
Demonstrates a group of Checkbutton widgets
'''
class MyGUI:
  # Constructor
  def __init__(self):
    # Create main window
    self.main_window = tkinter.Tk()

    # Create two frames:  One for checkbuttons
    # and another for regular Button widgets
    self.top_frame = tkinter.Frame(self.main_window)
    self.bottom_frame = tkinter.Frame(self.main_window)
    
    # Create three IntVar objects to use with
    # Checkbuttons
    self.cb_var1 = tkinter.IntVar()
    self.cb_var2 = tkinter.IntVar()
    self.cb_var3 = tkinter.IntVar()
    
    # Initialize intVars to 0 (unselected)
    # Note: must use set() method (NOT =)
    self.cb_var1.set(0)
    self.cb_var2.set(0)
    self.cb_var3.set(0)
    
    # Create Checkbutton widgets in top_frame
    self.cb1 = tkinter.Checkbutton(self.top_frame, \
               text='Option 1', variable=self.cb_var1)
    self.cb2 = tkinter.Checkbutton(self.top_frame, \
               text='Option 2', variable=self.cb_var2)
    self.cb3 = tkinter.Checkbutton(self.top_frame, \
               text='Option 3', variable=self.cb_var3)

    # Pack Checkbuttons
    self.cb1.pack()
    self.cb2.pack()
    self.cb3.pack()

    # Create OK button and Quit button
    self.ok_button = tkinter.Button(self.bottom_frame, \
                    text='OK', command=self.showChoice)
    self.quit_button = tkinter.Button(self.bottom_frame, \
                      text='Quit', command=self.main_window.destroy)

    # Pack Buttons
    self.ok_button.pack(side='left')
    self.quit_button.pack(side='left')

    # Pack frames
    self.top_frame.pack()
    self.bottom_frame.pack()
    
    # Start mainloop
    tkinter.mainloop()


  # ---------------------------------------------------------------------------
  # Event Handlers

  # Callback function that is invoked when OK button is clicked   
  def showChoice(self):
    # Create message string
    self.message = 'You selected:\n'

    # Determine which Checkbuttons are selected and
    # build message string accordingly
    if self.cb_var1.get() == 1:
        self.message = self.message + '1\n'
    if self.cb_var2.get() == 1:
        self.message = self.message + '2\n'
    if self.cb_var3.get() == 1:
        self.message = self.message + '3\n'

    # Display message in info dialog box.
    tkinter.messagebox.showinfo('Selection', self.message)

# Create instance of the MyGUI class
MyGUI()
