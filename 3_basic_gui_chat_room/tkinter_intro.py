#TKinter intro

import tkinter

#Define window

root = tkinter.Tk()
root.title("Let's Chat")
root.geometry('400x600')
root.resizable(0,0)

#Define colors
root_color = "#535657"
input_color = "#4f646f"
output_color = "#dee7e7"

root.config(bg=root_color)



#Define GUI Layout
#Define Frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)

input_frame.pack(pady=10)
output_frame.pack(pady=(0,10), padx=10, fill=tkinter.BOTH, expand=True)

#Define Widgets
message_entry = tkinter.Entry(input_frame, text="Enter a message", width=30)
send_button = tkinter.Button(input_frame, text="Send")
message_entry.grid(row=0, column=0, padx=10, pady=10)
send_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=5)


#Run the root windows mainloop()
root.mainloop()
