#TKinter intro

import tkinter

#Define window

root = tkinter.Tk()
root.title("Let's Chat")
root.geometry('400x600')
root.resizable(0,0)

#Define colors
root_color = "#535657"

root.config(bg=root_color)


#Run the root windows mainloop()
root.mainloop()
