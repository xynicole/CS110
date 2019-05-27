import tkinter
import kiloToMiles

# Converts kilometers to miles
# Displays result in label
# Demonstrates Entry Box without event,
# Model-View-Controller
class KiloConverterGUI:
  def __init__(self):

    # Create model, default state
    self.__model = kiloToMiles.KiloToMiles()
    
    # Create the main window
    self.__main_window = tkinter.Tk()

    # Create three frames to group widgets
    self.__top_frame = tkinter.Frame(self.__main_window) # Controller
    self.__mid_frame = tkinter.Frame(self.__main_window) # View
    self.__bottom_frame = tkinter.Frame(self.__main_window) #Controller

    # Create label and control for the top frame
    self.__prompt_label = tkinter.Label(self.__top_frame, \
                text='Enter a distance in kilometers:')
    self.__kilo_entry = tkinter.Entry(self.__top_frame, \
                                    width=10)

    # Pack top frame's widgets
    self.__prompt_label.pack(side='left')
    self.__kilo_entry.pack(side='left')

    # Create View for the middle frame
    self.__descr_label = tkinter.Label(self.__mid_frame, \
                             text='Converted to miles:')
    
    # Associate StringVar object with an output label
    # The set method can be used to
    # to store a string of blank characters
    #self.__value = tkinter.DoubleVar()
    self.__value = tkinter.StringVar()
    self.__value.set("%.2f" % 0)
    #self.__value.set("     ")
    #self.__value.set(0)

    # Create label and associate it with StringVar object
    # Any value stored in the StringVar object 
    # will automatically be displayed in the label
    self.__miles_label = tkinter.Label(self.__mid_frame, \
                                textvariable=self.__value)

    # Pack middle frame's widgets
    self.__descr_label.pack(side='left')
    self.__miles_label.pack(side='left')

    # Create button controls for bottom frame
    self.__calc_button = tkinter.Button(self.__bottom_frame, \
                                 text='Convert', \
                                 command=self.convert)
    self.__quit_button = tkinter.Button(self.__bottom_frame, \
                            text='Quit', \
                            command=self.__main_window.destroy)

    # Pack buttons
    self.__calc_button.pack(side='left')
    self.__quit_button.pack(side='left')

    # Pack frames
    self.__top_frame.pack()
    self.__mid_frame.pack()
    self.__bottom_frame.pack()

    # Start listener
    tkinter.mainloop()

  # ---------------------------------------------------------------------------
  # Event Handlers
  
  # Callback function for Convert button  
  def convert(self):
    # Set model value to value in entry box
    self.__model.set_kilo(float(self.__kilo_entry.get()))
                         
    # Convert miles to a string and store it
    # in the StringVar object
    # This will automatically
    # update the miles_label widget
    self.__value.set("%.2f" % self.__model.to_miles())
    #self.__value.set("%.2f" % self.__model.to_miles())
    self.__kilo_entry.delete(0, tkinter.END)  # Clear entry box

KiloConverterGUI()
