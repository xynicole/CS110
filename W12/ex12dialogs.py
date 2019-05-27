from tkinter import *
from tkinter.messagebox import *

'''
Demonstrates variety of messagebox dialogs
Arguments are: title for titlebar and message (both str)
Both askyesno() and askokcancel() return bool
'''

def main():
  win = Tk()
  messagebox.showinfo(
    'Using messagebox.showinfo()',
    "Sounds asterisk, displays 'i' icon and informative message")
  messagebox.showwarning(
    'Using messagebox.showwarning()', 
    "Sounds exclamation, displays rocket icon and warning message")
  messagebox.showerror(
    'Using messagebox.showerror()',
    "Sounds critical stop, displays 'x' icon and error message")
  answer = messagebox.askyesno(
    'Using messagebox.askyesno()',
    "No sound, displays '?' icon, asks question: yes == True, no == False")
  print("User selected", answer)
  selection = messagebox.askokcancel(
    'Using messagebox.askokcancel()',
    "No sound, displays '?' icon, Asks question: ok == True, cancel == False")
  print("User selected", selection)
                    
main()    
