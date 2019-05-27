from tkinter import *
from Lab11 import CounterWP


class Counter_GUI_WP:
    def __init__ (self):
#window
        self.__win = Tk()
        self.__top = Frame(self.__win)
        self.__mid = Frame(self.__win)
        self.__bottom = Frame(self.__win)

#model
        self.__model = CounterWP()
        self.__count_up = Button(self.__top, text = 'Count Up!', command = self.count_up)
        self.__count_down = Button(self.__top, text = 'Count Down', command = self.count_down)

#pack
        self.__count_up.pack(side = 'left')
        self.__count_down.pack(side = 'left')

        self.__reset_button = Button(self.__mid, text = 'RESET', command = self.reset)
        self.__prompt = Label(self.__mid, text = 'Set Counter:')
        self.__entry = Entry(self.__mid, width = 7)
        self.__entry.bind('<Return>',self.set_entry)
        self.__label = Label(self.__bottom, text = 'Count = ')
        
        self.__reset_button.pack(side = 'left')
        self.__prompt.pack(side = 'left')                             
        self.__entry.pack(side = 'left')
        self.__i_val = IntVar()
        self.__i_val.set (self.__model.get_value())
        
        self.__lval = Label(self.__bottom, textvariable = self.__i_val)
        self.__label.pack(side = 'left')
        self.__lval.pack(side = 'left')
        self.__top.pack()
        self.__mid.pack()
        self.__bottom.pack()

        mainloop()
        
    def count_up(self):
        self.__model.increment()
        self.__update_display()
    def count_down(self):
        if self.__is_not_negative():
            self.__model.decrement()
            
        else:
            print('Value already at zero!')
        self.__update_display()   
            
    def reset(self):
        self.__model = 0
        self.__update_display()
    def set_entry(self, event):
        
        
        if int(self.__entry.get()) >= 0:
            self.__model.setm(int(self.__entry.get())) 
            self.__update_display()
        else:
            print('Value can not be negative!')
        
        self.__entry.delete(0,END)

    def __is_not_negative(self):
        return self.__model.get_value() > 0
    
    def __can_decrement(self):
        if not self.__is_not_negative(self.__model):
            return warn()
            

    def __update_display(self):
        self.__i_val.set(self.__model.get_value())
        
    def __warn():
        messagebox.showwarning('Already at Zero!','Cannot go lower than Zero')
        
        
Counter_GUI_WP()        

        
