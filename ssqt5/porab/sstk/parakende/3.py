
# importing tkinter as tk to prevent any overlap with built in methods.
import tkinter as tk
# filedialog is used in this case to save the file path selected by the user.
from tkinter import filedialog

root = tk.Tk()
file_path = ""

def open_and_prep():
    # global is needed to interact with variables in the global name space
    global file_path
    # askopefilename is used to retrieve the file path and file name.
    file_path = filedialog.askopenfilename()

def process_open_file():
    global file_path
    # do what you want with the file here.
    if file_path != "":
        # opens file from file path and prints each line.
        with open(file_path,"r") as testr:
            for line in testr:
                print (line)

# create Button that link to methods used to get file path.
tk.Button(root, text="Open file", command=open_and_prep).pack()
# create Button that link to methods used to process said file.
tk.Button(root, text="Print Content", command=process_open_file).pack()

root.mainloop()
