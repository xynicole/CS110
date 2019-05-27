import tkinter
import kiloToMiles

'''
Converts kilometers to miles
Displays result in Label
'''
class KiloConverterGUI:
  # ---------------------------------------------------------------------------
  # Constructor
  def __init__(self):

    # Create instance of MODe_l
    self.__kilo_val = kiloToMiles.KiloToMiles()
    
    # Create the main window
    self.__main_window = tkinter.Tk()

    #--------------------------------------------------------------------------
    # Frames and widgets

    # Create three frames to group widgets
    self.__top_frame = tkinter.Frame()
    self.__mid_frame = tkinter.Frame()
    self.__bottom_frame = tkinter.Frame()

    # Create top frame widgets
    self.__kilo_entry_label = tkinter.Label(self.__top_frame, 
                text='Enter distance in kilometers: ')
    self.__kilo_entry = tkinter.Entry(self.__top_frame,
                                     width = 10)

    # use bind method to connect <Return> event to callback method
    self.__kilo_entry.bind('<Return>', self.convert_from_entry)

    # Pack top frame widgets
    self.__kilo_entry_label.pack(side='left')
    self.__kilo_entry.pack(side='left')

    # Create middle frame widgets
    # Associate StringVar with label for output
    # Use set method to initialize    
    self.__value1 = tkinter.StringVar()
    self.__value1.set("%.2f kilometers" % self.__kilo_val.get_kilo())

    # Create label and associate with StringVar
    # Value stored in StringVar will be
    #  automatically displayed in label
    self.__kilo_label = tkinter.Label(self.__mid_frame,
                                     textvariable = self.__value1)
    self.__middle_label = tkinter.Label(self.__mid_frame, 
                                       text=' converted to miles = ')
    
    # Associate StringVar with label for output
    # Use set method to initialize
    self.__value2 = tkinter.StringVar()
    self.__value2.set("%.2f miles" % self.__kilo_val.to_miles())

    # Create label and associate with StringVar
    # Value stored in StringVar will be
    #  automatically displayed in label
    self.__miles_label = tkinter.Label(self.__mid_frame, 
                                textvariable=self.__value2)

    # Pack middle frame widgets
    self.__kilo_label.pack(side='left')
    self.__middle_label.pack(side='left')
    self.__miles_label.pack(side='left')

    # Create bottom frame button widgets
    self.__convert_button = tkinter.Button(self.__bottom_frame, 
                                 text='Convert', 
                                 command=self.convert)
    self.__quit_button = tkinter.Button(self.__bottom_frame, 
                            text='Quit', 
                            command=self.__main_window.destroy)

    # Pack buttons
    self.__convert_button.pack(side='left')
    self.__quit_button.pack(side='left')

    # Pack frames
    self.__top_frame.pack()
    self.__mid_frame.pack()
    self.__bottom_frame.pack()

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
      # Get value from kilo_entry widget and set mode_l
      self.__kilo_val.set_kilo(float(self.__kilo_entry.get()))

      #
      self.__value1.set("%.2f kilometers" % self.__kilo_val.get_kilo())

      # Convert kilometers to miles and 
      # store formatted result in StringVar object
      # Wll automatically update milesLabel widget
      self.__value2.set("%.2f miles" % self.__kilo_val.to_miles())
      
    # Entry box input was inappropriate
    except ValueError as err:
      tkinter.messagebox.showerror('Kilos to Miles', 
                                  "Must provide valid input: %s" % err)
      self.__kilo_val.reset_kilo()
      self.__value1.set("%.2f kilometers" % self.__kilo_val.get_kilo())
      self.__value2.set("%.2f miles" % self.__kilo_val.to_miles())
    finally:
      self.__kilo_entry.delete(0, tkinter.END)  # Clear entry box

# Create instance of KiloConverterGUI class
KiloConverterGUI()
