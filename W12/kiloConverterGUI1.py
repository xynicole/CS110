import tkinter
import tkinter.messagebox
import kiloToMiles

'''
Converts kilometers to miles
Displays result in dialog box
'''
class KiloConverterGUI:
  # ---------------------------------------------------------------------------
  # Constructor
  def __init__(self):
    # Create instance of MODEL
    self.__kilo_val = kiloToMiles.KiloToMiles()

    # Create the main window
    self.__main_window = tkinter.Tk()

    #--------------------------------------------------------------------------
    # Frames and widgets

    # Create two frames to group widgets
    self.__top_Frame = tkinter.Frame()
    self.__bottom_Frame = tkinter.Frame()

    # Create the widgets for the top frame
    self.__kilo_entry_label = tkinter.Label(self.__top_Frame, 
                text='Enter a distance in kilometers: ')
    self.__kilo_entry = tkinter.Entry(self.__top_Frame, 
                                     width=10)
    # use bind method to connect <Return> event to callback method
    self.__kilo_entry.bind('<Return>', self.convert_from_entry)

    # Pack top frame widgets
    self.__kilo_entry_label.pack(side='left')
    self.__kilo_entry.pack(side='left')

    # Create the button widgets for the bottom frame
    self.__convert_button = tkinter.Button(self.__bottom_Frame, 
                                          text='Convert', 
                                          command=self.convert)
    self.__quit_button = tkinter.Button(self.__bottom_Frame, 
                                       text='Quit', 
                                       command=self.__main_window.destroy)
    # Pack the buttons
    self.__convert_button.pack(side='left')
    self.__quit_button.pack(side='left')

    # Pack the frames
    self.__top_Frame.pack()
    self.__bottom_Frame.pack()


    #--------------------------------------------------------------------------
    # Enter the tkinter main loop
    tkinter.mainloop()

  #----------------------------------------------------------------------------
  # Event Handlers

  # Callback method for entry box
  # Invokes button callback to do work
  def convert_from_entry(self, event):
    self.convert()

  # Callback method for compute button
  # Note use of exception handling instead of validation
  def convert(self):
    try:
      # Get value from kilo_entry widget and set model
      self.__kilo_val.set_kilo(float(self.__kilo_entry.get()))

      # Convert and display results in info dialog box
      # Uses 'toString' of self.__kilo_val
      tkinter.messagebox.showinfo('Kilos to Miles', 
                                  str(self.__kilo_val))
    except ValueError as err:
      tkinter.messagebox.showerror('Kilos to Miles', 
                                  "Must pro_Vide valid input: %s" % err)
    finally:
      self.__kilo_entry.delete(0, tkinter.END)  # Clear entry box
#----------------------------------------------------------------------------__

# Create instance of KiloConverterGUI class
KiloConverterGUI()
