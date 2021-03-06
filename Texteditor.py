import tkinter as tk
import tkinter.colorchooser as colbox
import tkinter.filedialog as fbox

# list of keywords
list = ["auto","break","case","char","const","continue","default","do","double","else",
        "enum","extern","float","for","goto","if","#include","int","long","main",
        "public","register","return","short","signed","sizeof","static","struct","switch",
        "typedef","union","unsigned","volatile","while","void","%d","%f","%c",]

# creating window***********
window = tk.Tk()
window.title("Notepad++ Spoof")
window.geometry("930x650")

# creating MENUBAR ***************
menu1 = tk.Menu(window)
window.config(menu=menu1, bg="white")
fileMenu = tk.Menu(menu1, tearoff=False)
editMenu = tk.Menu(menu1, tearoff=False)


def intro():
    frame2 = tk.Toplevel(window)

    display = tk.Label(frame2, text=(""" Hey!!!\nWelcome to the world of Python.\n
    This is a Text Editor based on Notepad++.\n
    Team members : \n1)Sandeep Das \n2)Akanksha Sinha\n\n\nAll rights reserved©"""), width=50, height=30,
                       bg="white", foreground="black", font=('Arial Rounded MT', 15, 'bold'))

    display.pack()

color = tk.Menu(menu1, tearoff=False)
about = tk.Menu(menu1, tearoff=False)
options = tk.Menu(menu1, tearoff=False)
menu1.add_cascade(label="File", menu=fileMenu)
menu1.add_cascade(label="Edit", menu=editMenu)
menu1.add_cascade(label="Color", menu=color)
menu1.add_cascade(label="Options", menu=options)
menu1.add_cascade(label="About", menu=about)
about.add_command(label="Info", command=intro)



# functions in file menu***************
def openfile(event=None):
    filename = fbox.askopenfilename(initialdir=r"./", title="Open file", filetypes=[("All files", "*.*")])

def save(event=None):
    filename = fbox.asksaveasfilename(initialdir=r"./", title="Save file", filetypes=[("All files", "*.*")])


# sub-menus of file menu****************
fileMenu.add_command(label="New", accelerator='Ctrl+n', command=lambda event: textbox.delete(1.0, tk.END))
window.bind("<Control-n>", lambda: textbox.delete(1.0, tk.END))

fileMenu.add_command(label="Open", accelerator='Ctrl+o', command=openfile)
window.bind("<Control-o>", openfile)

fileMenu.add_command(label="Save", accelerator='Ctrl+s', command=save)
window.bind("<Control-s>", save)

fileMenu.add_command(label="Save as", accelerator='Ctrl+Shift+s', command=save)
window.bind("<Control-Shift-s>", save)

fileMenu.add_separator()
fileMenu.add_command(label="Close", underline=4, command=window.quit)

# sub-menus of edit menu ****************
editMenu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: textbox.event_generate("<Control c>"))
editMenu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: textbox.event_generate("<Control v>"))
editMenu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: textbox.event_generate("<Control x>"))
editMenu.add_command(label='Clear All', accelerator='Ctrl+Alt+X', command=lambda: textbox.delete(1.0, tk.END))

options.add_command(label="Compile", accelerator="Alt+Shift+F9", command=lambda: textbox.event_generate("Alt-Shift-F9"))
options.add_command(label="Run", accelerator="Alt+Shift+F10", command=lambda: textbox.event_generate("Alt-Shift-F10"))

# creating scroll bar and source code textbox
frame1 = tk.Frame(window)
# scrollbar
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# text box
l1 = "1.0"


def retrieve_input(event):
    z = textbox.index(tk.INSERT)
    global l1
    inputValue = textbox.get(l1, z)
    l1 = z
    l = inputValue.split()

    for i in l:

        if i in list:

            textbox.tag_add(i, "%d.%d" % (int(z[0]), int(z[2]) - len(i) - 1), "%d.%d" % (int(z[0]), int(z[2])))
            textbox.tag_configure(i, foreground="yellow", font='italic')


# textbox.insert(tk.INSERT,inputValue)
textbox = tk.Text(frame1, wrap=tk.NONE, yscrollcommand=scrollbar.set, width=100, height=35, bg="black",
                  foreground="white", highlightcolor="yellow", font=('Arial', 12), insertbackground="Yellow")


window.bind("<space>", retrieve_input)
scrollbar.config(command=textbox.yview)

def choosecolor1():
    color = colbox.askcolor()
    textbox.config(bg=color[1])
    if (color == "white"):
        window.config(bg="white")
    else:
        window.config(bg="blue4")

def choosecolor():
    color = colbox.askcolor()
    textbox.config(foreground=color[1])


color.add_command(label="Change IDE Color", command=choosecolor1)
color.add_command(label="Change Text Color", command=choosecolor)

# Aligning Source code textbox**************
textbox.pack(side=tk.LEFT)
frame1.grid(row=0, column=1, columnspan=20, padx=10)

# **************************************************
window.mainloop()