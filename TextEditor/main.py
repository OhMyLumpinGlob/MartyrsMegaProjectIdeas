from Tkinter import *

import Tkinter, os
import tkMessageBox

top = Tk()

def Cut():
    top.clipboard_clear()
    top.clipboard_append(text_display.get(SEL_FIRST,SEL_LAST))
    text_display.delete(SEL_FIRST,SEL_LAST)

def Copy():
    top.clipboard_clear()
    top.clipboard_append(text_display.get(SEL_FIRST,SEL_LAST))

def Paste():
    text_display.insert(INSERT,top.clipboard_get())

def About():
    about_window = Toplevel()
    label = Label(about_window,text="OhMyLumpinGlob's Text Editor of Death. Use with care. Or just don't use, it's pretty awful...")
    label.pack(side=TOP)
    ok_button = Button(about_window, text='OK', command=about_window.destroy)
    ok_button.pack(side=BOTTOM)

def Help():
    help_window = Toplevel()
    label = Label(help_window,text="No-one can help you now, buddy")
    label.pack(side=TOP)
    ok_button = Button(help_window, text="I'm not your buddy, guy!", command=help_window.destroy)
    ok_button.pack(side=BOTTOM)

def New():
    def start_new_file():
        text_display.delete('1.0', END)
        new_file_window.destroy()
    def cancel_new_file():
        new_file_window.destroy()
    new_file_window = Toplevel()
    label = Label(new_file_window,text='Discard current file and start a new text document?')
    label.pack(side=TOP)
    ok_button = Button(new_file_window, text='OK', command=start_new_file)
    ok_button.pack(side=LEFT)
    cancel_button = Button(new_file_window, text='Cancel', command=cancel_new_file)
    cancel_button.pack(side=RIGHT)

def Save():
    def save_file_as():
        if not os.path.exists('saves'):
            os.makedirs('saves')
        filename = 'saves/' + entry.get()
        f = open(filename, 'w+')
        f.write(text_display.get('1.0',END))
        f.close()
        save_file_window.destroy()
    save_file_window = Toplevel()
    label = Label(save_file_window,text='Save as:')
    label.pack(side=LEFT)
    entry = Entry(save_file_window)
    entry.pack()
    save_as_button = Button(save_file_window, text='OK', command=save_file_as)
    save_as_button.pack(side=RIGHT)

def Open():
    def open_file():
        if not os.path.exists('saves'):
            os.makedirs('saves')
        try:
            filename = 'saves/' + entry.get()
            f = open(filename, 'r')
            text_display.delete('1.0', END)
            text_display.insert('1.0', f.read())
            f.close()
        except:
            file_not_found_window = Toplevel()
            label = Label(file_not_found_window, text='File Not Found')
            label.pack()
        open_file_window.destroy()
    open_file_window = Toplevel()
    label = Label(open_file_window,text='Open:')
    label.pack(side=LEFT)
    entry = Entry(open_file_window)
    entry.pack()
    open_file_button = Button(open_file_window, text='OK', command=open_file)
    open_file_button.pack(side=RIGHT)

def Exit():
    top.destroy()
    top.quit()

text_display = Text(top)

menu_bar = Menu(top)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=New)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Exit",command=Exit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=Cut)
edit_menu.add_command(label="Copy", command=Copy)
edit_menu.add_command(label="Paste", command=Paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=About)
about_menu.add_command(label="Help", command=Help)
menu_bar.add_cascade(label="About", menu=about_menu)

text_display.pack()

top.config(menu=menu_bar)
top.mainloop()
