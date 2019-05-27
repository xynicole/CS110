import tkinter
import tkinter.messagebox

'''
Demonstrates a group of Radiobutton widgets
'''
class MyGUI:
  # Constructor
  def __init__(self):
    # Create main window
    self.main_window = tkinter.Tk()

    # Create two frames. One for Radiobuttons
    # Another for regular Button widgets
    self.top_frame = tkinter.Frame(self.main_window)
    self.bottom_frame = tkinter.Frame(self.main_window)
    
    # Create IntVar object to use with Radiobuttons
    self.radio_var = tkinter.IntVar()
    
    # Set intVar to 1
    # Note that set() method must be used (NOT =)
    self.radio_var.set(1)

    # Create Radiobutton widgets in top_frame
    self.rb1 = tkinter.Radiobutton(self.top_frame, \
               text='Option 1', variable=self.radio_var, \
               value=1)
    self.rb2 = tkinter.Radiobutton(self.top_frame, \
               text='Option 2', variable=self.radio_var, \
               value=2)
    self.rb3 = tkinter.Radiobutton(self.top_frame, \
               text='Option 3', variable=self.radio_var, \
               value=3)

    # Pack Radiobuttons
    self.rb1.pack()
    self.rb2.pack()
    self.rb3.pack()

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
    
    # Start the mainloop
    tkinter.mainloop()

  # Callback method invoked when OK button is clicked
  def showChoice(self):
      tkinter.messagebox.showinfo('Selection', 'You selected option ' +\
                            str(self.radio_var.get()))

# Create instance of MyGUI class
MyGUI()
