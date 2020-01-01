import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

read_file = ""  # The path of the file which will be cut

def cut_algorithm(to_keep):
    """
    Cuts the selected file based on the class names that are in to_keep.
    :param to_keep: A list that holds the class names which the user wants to keep.
    :return: A string that holds all the style rules which have been kept.
    """
    file = open(read_file, "r")
    new_file_content = ""  # String to hold the style rules that are kept
    get_styles = 0  # Flag for if an item from to_keep is found in a line
    get_media = 0  # Flag for if a media rule is present
    flag = 0  # Flag gets activated if a "}" has already been claimed by a previous if-statment for belonging to a style rule. In short, it checks if the "}" belongs to a media rule.

    for line in file:
        flag = 0
        if get_styles == 1 and "}" not in line:
            new_file_content += line
        if is_in_line(to_keep, line) == True:
            new_file_content += line
            get_styles = 1
        if get_styles == 1 and "}" in line:
            new_file_content += line
            get_styles = 0
            flag = 1

        if is_in_line(to_keep, line) == False and "{" in line:
            get_styles = -1
        if get_styles == -1 and "}" in line:
            get_styles = 0
            flag = 1

        if "media" in line:
            new_file_content += line
            get_media = 1

        if get_media == 1 and "}" in line and get_styles == 0 and flag == 0:
            new_file_content += line
            get_media = 0

    return new_file_content


def open_explorer():
    """
    Opens the file explorer so a user can find and select a .CSS file to cut.
    :return: None
    """
    filename = filedialog.askopenfilename(initialdir="/", title = "Select File", filetypes = (("CSS Files", "*.css"), ("Text Files", "*.txt")))
    if filename != "":
        global  read_file
        read_file = filename
        stripped = read_file.split("/")
        currFile.configure(text="File: " + stripped[-1])

def cut_file():
    """
    Executes the process of cutting the selected file.
    :return: None
    """
    if read_file == "":
        messagebox.showerror("Error", "You must select a file to cut")
        print(read_file)
    else:
        to_keep = [textbox_1.get(), textbox_2.get(), textbox_3.get(), textbox_4.get(), textbox_5.get(), textbox_6.get()]
        to_keep = list(filter(lambda a: a != "", to_keep))
        new_file_content = cut_algorithm(to_keep)
        file = open("Output.css", "w")
        file.write(new_file_content)
        file.close()
        messagebox.showinfo("Done!", "Your new file is located at " + os.getcwd() + "\Output.css")

def is_in_line(to_keep, line):
    """
    Checks if any of the class names in to_keep are in the line
    :param to_keep: A list that holds the class names which the user wants to keep.
    :param line: A single line in the file that is currently being examined.
    :return: Returns True if a class name from to_keep is in the line. False otherwise.
    """
    for item in to_keep:
        if item in line:
            return True
    return False


# Creation of tkinter window
root = tk.Tk();
root.title('CSS Cutter')
root.geometry("490x240")
root.resizable(0, 0)

# Creation of tkinter items
openFileButton = tk.Button(root, text = "Open File", pady = 5, width = "30", fg = "#fff", bg = "#496F9B", command = open_explorer)
cutFileButton = tk.Button(root, text = "Cut File", pady = 5, width = "64", fg = "#fff", bg = "#496F9B", command = cut_file)
howToUse = tk.Label(root, text = "Enter class names and / or prefixes that you want to keep")
currFile = tk.Label(root, text = "No File Selected")
textbox_1 = tk.Entry(root, width = "36")
textbox_2 = tk.Entry(root, width = "36")
textbox_3 = tk.Entry(root, width = "36")
textbox_4 = tk.Entry(root, width = "36")
textbox_5 = tk.Entry(root, width = "36")
textbox_6 = tk.Entry(root, width = "36")

# Placement of tkinter items
openFileButton.place(x=15, y=15)
currFile.place(x=247, y=21)
howToUse.place(x=13, y=60)
textbox_1.place(x=15, y=90)
textbox_2.place(x=15, y=120)
textbox_3.place(x=15, y=150)
textbox_4.place(x=250, y=90)
textbox_5.place(x=250, y=120)
textbox_6.place(x=250, y=150)
cutFileButton.place(x=15, y=190)

root.mainloop()