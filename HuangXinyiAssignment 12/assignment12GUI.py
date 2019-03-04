'''
Xinyi Huang
xhuang78@binghamton.edu
Jia Yang B58
Assignment12
'''
'''
With the Patron, Book, and Library classes serving as the model classes,
create a front-end GUI for a library using the model-view-controller pattern

'''

from tkinter import *
from patron import *
from book import *
from library import *
from libraryModule import *


class my_GUI:
  def __init__(self):
#window
    self.__win = Tk()
    self.__win.title("BOOK CHECKER")
    self.__library = Library("PYTHONVILLE HOMETOWN LIBRARY")

    self.__checkout_title_value = None
    self.__checkout_patron_value = None
    self.__add_name_value = None
    self.__add_author_value = None


    


    self.__toplabel = Label(self.__win, text = "PYTHONVILLE HOMETOWN LIBRARY")
    self.__toplabel.grid(row=0, column=3)
# check out books label and return books label

    self.__lab_check = Label(self.__win, text = "Check Out Books")
    self.__lab_check.grid(row=1, rowspan=1,column=2, columnspan=1)
    self.__lab_return = Label(self.__win, text = "Return Books")
    self.__lab_return.grid(row=1, rowspan=1,column=4, columnspan=1)   
    
#check out + return title label and entry
    #check out label
    self.__lab_che_title = Label(self.__win, text = "Title")
    self.__lab_che_title.grid(row=2, rowspan=1,column=1, columnspan=1)
    #check out entry
    self.__entry_title = Entry(self.__win, width=50)
    self.__entry_title.grid(row=2,rowspan=1, column=2, columnspan=1)
    self.__entry_title.bind('<Return>', self.checkout_title_entry_eh)
    #return label
    self.__lab_re_title = Label(self.__win, text = "Title")
    self.__lab_re_title.grid(row=2, rowspan=1,column=3, columnspan=1)
    #retrun entry
    self.__entry_retitle = Entry(self.__win, width=50)
    self.__entry_retitle.grid(row=2,rowspan=1, column=4, columnspan=1)
    self.__entry_retitle.bind('<Return>', self.set_return) 
   

#check out + retrun patron label and entry
    #check out label
    self.__lab_patron = Label(self.__win, text = "Patron")
    self.__lab_patron.grid(row=3,rowspan=1, column=1, columnspan=1)
    #check out entry
    self.__entry_patron = Entry(self.__win,width=50)
    self.__entry_patron.grid(row=3, rowspan=1, column=2, columnspan=1)
    self.__entry_patron.bind('<Return>', self.checkout_patron_entry_eh)
    #patron label
    self.__lab_repatron = Label(self.__win, text = "Patron")
    self.__lab_repatron.grid(row=3,rowspan=1, column=3, columnspan=1)
    #patron entry
    self.__va_paentry = StringVar()
    self.__va_paentry.set("")
    self.__paentry = Label(self.__win, textvariable = self.__va_paentry)
    self.__paentry.grid(row=3,rowspan=1, column=4, columnspan=1)

    
#check out + return button
    #check out
    self.__button_checkout = Button(self.__win, text = "Check Out Books", \
                                    command = self.checkout)
    self.__button_checkout.grid(row=4,rowspan=1, column=2, columnspan=1)
    self.__button_checkout.configure(state="disabled")
    
    #return
    self.__button_return = Button(self.__win, text = "Return Book", \
                                    command = self.return_book)
    self.__button_return.grid(row=4,rowspan=1, column=4, columnspan=1)
    self.__button_return.configure(state="disabled")

#check out + return status
    #check out
    self.__lab_statu = Label(self.__win, text= "Status")
    self.__lab_statu.grid(row=5, rowspan=1, column=1, columnspan=1)
    self.__var_check = StringVar()
    self.__var_check.set("No Transactions")

    self.__lab_varcheck = Label(self.__win, textvariable=self.__var_check)
    self.__lab_varcheck.grid(row=5, rowspan=1, column=2, columnspan=1)

    #return
    self.__lab_restatu = Label(self.__win, text= "Status")
    self.__lab_restatu.grid(row=5, rowspan=1, column=3, columnspan=1)
    self.__var_return = StringVar()
    self.__var_return.set("No Transactions")

    self.__lab_varreturn = Label(self.__win, textvariable=self.__var_return)
    self.__lab_varreturn.grid(row=5, rowspan=1, column=4, columnspan=1)

######################################
#search book and patron labels
    self.__lab_search = Label(self.__win, text = "SEARCH")
    self.__lab_search.grid(row=6, column=3)
    
    self.__lab_book = Label(self.__win, text = "Book")
    self.__lab_book.grid(row=7, rowspan=1,column=2, columnspan=1)
    self.__lab_patron = Label(self.__win, text = "Patron")
    self.__lab_patron.grid(row=7, rowspan=1,column=4, columnspan=1)
    
#book + patron title,name label and entry
    self.__lab_bk_title = Label(self.__win, text = "Title")
    self.__lab_bk_title.grid(row=8, rowspan=1,column=1, columnspan=1)
    #book entry
    self.__entry_bktitle = Entry(self.__win, width=50)
    self.__entry_bktitle.grid(row=8,rowspan=1, column=2, columnspan=1)
    self.__entry_bktitle.bind('<Return>', self.search_book)
    #patron name label
    self.__lab_nm_title = Label(self.__win, text = "Title")
    self.__lab_nm_title.grid(row=8, rowspan=1,column=3, columnspan=1)
    #name entry
    self.__entry_nmtitle = Entry(self.__win, width=50)
    self.__entry_nmtitle.grid(row=8,rowspan=1, column=4, columnspan=1)
    self.__entry_nmtitle.bind('<Return>', self.search_name)


#book + patron
    self.__va_bkstatus = StringVar()
    self.__va_bkstatus.set("")
    self.__status_book = Label(self.__win, textvariable=self.__va_bkstatus)
    self.__status_book.grid(row=9, rowspan=1, column=2, columnspan = 1)
    
    self.__va_pastatus= StringVar()
    self.__va_pastatus.set("")
    self.__status_patron = Label(self.__win,textvariable=self.__va_pastatus)
    self.__status_patron.grid(row=9, rowspan=1, column=4, columnspan = 1)

#book + patron status
    #book
    self.__lab_bkstatu = Label(self.__win, text= "Status")
    self.__lab_bkstatu.grid(row=10, rowspan=1, column=1, columnspan=1)
    
    self.__var_book = StringVar()
    self.__var_book.set("No Transactions")

    self.__lab_varbook = Label(self.__win, textvariable=self.__var_book)
    self.__lab_varbook.grid(row=10, rowspan=1, column=2, columnspan=1)

    #return
    self.__lab_pastatu = Label(self.__win, text= "Status")
    self.__lab_pastatu.grid(row=10, rowspan=1, column=3, columnspan=1)
    self.__var_patron = StringVar()
    self.__var_patron.set("No Transactions")

    self.__lab_varpatron = Label(self.__win, textvariable=self.__var_patron)
    self.__lab_varpatron.grid(row=10, rowspan=1, column=4, columnspan=1)    

###################################
#membership join+leave labels
    self.__lab_member = Label(self.__win, text = "MEMBERSHIP")
    self.__lab_member.grid(row=11, column=3)
    
    self.__lab_join = Label(self.__win, text = "Join")
    self.__lab_join.grid(row=12, rowspan=1,column=2, columnspan=1)
    self.__lab_leave = Label(self.__win, text = "Leave")
    self.__lab_leave.grid(row=12, rowspan=1,column=4, columnspan=1)
    
#join + leave name label and entry
    self.__lab_jo_name = Label(self.__win, text = "Name")
    self.__lab_jo_name.grid(row=13, rowspan=1,column=1, columnspan=1)
    #join entry
    self.__entry_joname = Entry(self.__win, width=50)
    self.__entry_joname.grid(row=13,rowspan=1, column=2, columnspan=1)
    self.__entry_joname.bind('<Return>', self.add)
    #leave name label
    self.__lab_le_name = Label(self.__win, text = "Name")
    self.__lab_le_name.grid(row=13, rowspan=1,column=3, columnspan=1)
    #name entry
    self.__entry_lename = Entry(self.__win, width=50)
    self.__entry_lename.grid(row=13,rowspan=1, column=4, columnspan=1)
    self.__entry_lename.bind('<Return>', self.leave)    

#join + leave status
    #join
    self.__lab_jostatu = Label(self.__win, text= "Status")
    self.__lab_jostatu.grid(row=14, rowspan=1, column=1, columnspan=1)
    self.__var_join = StringVar()
    self.__var_join.set("No Transactions")

    self.__lab_varbook = Label(self.__win, textvariable=self.__var_join)
    self.__lab_varbook.grid(row=14, rowspan=1, column=2, columnspan=1)

    #leave
    self.__lab_lestatu = Label(self.__win, text= "Status")
    self.__lab_lestatu.grid(row=14, rowspan=1, column=3, columnspan=1)
    self.__var_leave = StringVar()
    self.__var_leave.set("No Transactions")

    self.__lab_varpatron = Label(self.__win, textvariable=self.__var_leave)
    self.__lab_varpatron.grid(row=14, rowspan=1, column=4, columnspan=1)   

#####################################
#book collection  labels
    self.__lab_collect = Label(self.__win, text = "BOOK COLLECTION")
    self.__lab_collect.grid(row=15, column=3)

#title  label and entry
    #title left label
    self.__lab_lf_title = Label(self.__win, text = "Title")
    self.__lab_jo_name.grid(row=16, rowspan=1,column=1, columnspan=1)
    #title left entry
    self.__entry_lftitle = Entry(self.__win, width=50)
    self.__entry_lftitle.grid(row=16,rowspan=1, column=2, columnspan=1)
    self.__entry_lftitle.bind('<Return>', self.add_name_eh)
    #title right label
    self.__lab_rt_title = Label(self.__win, text = "Title")
    self.__lab_rt_title.grid(row=16, rowspan=1,column=3, columnspan=1)
    #title right entry
    self.__entry_rttitle = Entry(self.__win, width=50)
    self.__entry_rttitle.grid(row=16,rowspan=1, column=4, columnspan=1)
    self.__entry_rttitle.bind('<Return>', self.set_entry)

#author label and entry
    #author left label
    self.__lab_lf_author = Label(self.__win, text = "Author")
    self.__lab_lf_author.grid(row=17, rowspan=1,column=1, columnspan=1)
    #author left entry
    self.__entry_lfauthor = Entry(self.__win, width=50)
    self.__entry_lfauthor.grid(row=17,rowspan=1, column=2, columnspan=1)
    self.__entry_lfauthor.bind('<Return>', self.add_author_eh)
    #author right label
    self.__lab_rt_author = Label(self.__win, text = "Author")
    self.__lab_rt_author.grid(row=17, rowspan=1,column=3, columnspan=1)
    #author right entry
    self.__va_rtauthor = StringVar()
    self.__va_rtauthor.set("")
    self.__rtauthor = Label(self.__win, textvariable = self.__va_rtauthor)
    self.__rtauthor.grid(row=17,rowspan=1, column=4, columnspan=1)
  

#add + remove button
    #add book
    self.__button_add = Button(self.__win, text = "Add Book", \
                                    command = self.add_book)
    self.__button_add.grid(row=18,rowspan=1, column=2, columnspan=1)
    self.__button_add.configure(state="disabled")
    
    #remove
    self.__button_remove = Button(self.__win, text = "Remove Book", \
                                    command = self.remove_book)
    self.__button_remove.grid(row=18,rowspan=1, column=4, columnspan=1)
    self.__button_remove.configure(state="disabled")

#add + remove status
    #add
    self.__lab_addstatu = Label(self.__win, text= "Status")
    self.__lab_addstatu.grid(row=19, rowspan=1, column=1, columnspan=1)
    self.__var_add = StringVar()
    self.__var_add.set("No Transactions")

    self.__lab_varadd = Label(self.__win, textvariable=self.__var_add)
    self.__lab_varadd.grid(row=19, rowspan=1, column=2, columnspan=1)

    #remove
    self.__lab_remstatu = Label(self.__win, text= "Status")
    self.__lab_remstatu.grid(row=19, rowspan=1, column=3, columnspan=1)
    self.__var_remove = StringVar()
    self.__var_remove.set("No Transactions")

    self.__lab_varremove = Label(self.__win, textvariable=self.__var_remove)
    self.__lab_varremove.grid(row=19, rowspan=1, column=4, columnspan=1)
    
    
    mainloop()



#remove book entry box EH
  def set_entry(self,event):
####    #if not self.__is_string(set_entry):
####      #return warn()
##    if self.__entry_title.get() and self.__entry_patron.get():
##      self.__button_checkout.configure(state="normal")
######    if self.__entry_retitle.get():
######      self.__button_return.configure(state="normal")
##    if self.__entry_lftitle.get() and self.__entry_lfauthor.get():
##      self.__button_add.configure(state="normal")
    if self.__entry_rttitle.get():
      book = self.__library.get_book(self.__entry_rttitle.get())
      if book:
        self.__va_rtauthor.set(book.get_author())
        self.__button_remove.configure(state="normal")
      else:
        self.__var_remove.set(self.__library.get_transaction_status())
      
#return books entry box
  def set_return(self,event):
    book = self.__library.get_book(self.__entry_retitle.get())
    if bool(book) and book.is_checked_out():
      self.__va_paentry.set(str(book.get_patron()))
      self.__button_return.configure(state="normal")
    else:
      self.__var_return.set(self.__library.get_transaction_status())


  def add_name_eh(self,event):
    self.__add_name_value = self.__entry_lftitle.get()
    if bool(self.__add_author_value) and bool(self.__add_name_value):
      self.__button_add.configure(state="normal")
      
  def add_author_eh(self,event):
    self.__add_author_value =self.__entry_lfauthor.get()
    if bool(self.__add_author_value) and bool(self.__add_name_value):
      self.__button_add.configure(state="normal")



  def checkout_title_entry_eh(self, event):
    self.__checkout_title_value = self.__entry_title.get()
    if bool(self.__checkout_title_value) and bool(self.__checkout_patron_value):
      self.__button_checkout.configure(state="normal")

  def checkout_patron_entry_eh(self, event):
    self.__checkout_patron_value = self.__entry_patron.get()
    if bool(self.__checkout_patron_value) and bool(self.__checkout_title_value):
      self.__button_checkout.configure(state="normal")
      
         
#check out book EH
  def checkout(self):
    book = self.__library.get_book(self.__checkout_title_value)
    patron = self.__library.get_patron(self.__checkout_patron_value)
    if book and patron:
      book.borrow_me(patron)
      self.__var_check.set(book.get_transaction_status())
    else:
      self.__var_check.set(self.__library.get_transaction_status())
    #reset
    self.__button_checkout.configure(state="disabled")
    self.__entry_title.delete(0, END)
    self.__entry_patron.delete(0, END)
    self.__checkout_title_value = None
    self.__checkout_patron_value = None

  #def checkout_title_entry_handler(self, event)

# return book EH
  def return_book(self):
    book = self.__library.get_book(self.__entry_retitle.get())
    if book:
      book.return_me()
      self.__var_return.set(book.get_transaction_status())
    else:
      self.__var_return.set(self.__library.get_transaction_status())
    #reset
    self.__button_return.configure(state="disabled")
    self.__entry_retitle.delete(0, END)
    self.__va_paentry.set("")



#search book
  def search_book(self,event):
    book = self.__library.get_book(self.__entry_bktitle.get())
    self.__var_book.set(self.__library.get_transaction_status())
    if bool(book):
      self.__va_bkstatus.set(str(book))
    else:
      self.__va_bkstatus.set("")
    self.__entry_bktitle.delete(0, END)

#search patron
  def search_name(self,event):
    patron =self.__library.get_patron(self.__entry_nmtitle.get())
    self.__var_patron.set(self.__library.get_transaction_status())
    if bool(patron):
      self.__va_pastatus.set(str(patron))
    else:
      self.__va_pastatus.set("")
    self.__entry_nmtitle.delete(0, END)
    
#membership join 
  def add(self,event):
    self.__library.add_patron(Patron(self.__entry_joname.get()))
    self.__var_join.set(self.__library.get_transaction_status())
    self.__entry_joname.delete(0, END)
                              
#membershio leave
  def leave(self,event):
    self.__library.remove_patron(self.__entry_lename.get())
    self.__var_leave.set(self.__library.get_transaction_status())
    self.__entry_lename.delete(0, END)    
                              

#book collection  add
  def add_book(self):
    self.__library.add_book(Book(self.__entry_lftitle.get(), \
    self.__entry_lfauthor.get()))
    self.__var_add.set(self.__library.get_transaction_status())
                                 
    self.__button_add.configure(state="disabled")
    self.__entry_lftitle.delete(0, END)
    self.__entry_lfauthor.delete(0, END)
    self.__add_name_value = None
    self.__add_author_value = None

#book collection remove
  def remove_book(self):
    self.__library.remove_book(self.__entry_rttitle.get())
    self.__var_remove.set(self.__library.get_transaction_status())
    self.__button_remove.configure(state="disabled")
    self.__entry_rttitle.delete(0, END)
    self.__va_rtauthor.set("")
    
                                 



my_GUI()
     


    
    
    
    

