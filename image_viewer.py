
import tkinter as tk
from tkinter import filedialog
from os import listdir
from tkinter.constants import E, SUNKEN, W
# for using different type of images
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image_viewer")
root.iconbitmap(
    ".\\picture_photo_image_icon_131252.ico")


def get_path(file):
    path = file.split("/")
    path.pop()
    path = "/".join(path)
    return path


def get_list(path):
    files = []
    for i in listdir(path):
        if ".jpg" in i:
            files.append(i)
    for i in range(len(files)):
        files[i] = "/".join([path, files[i]])
    return files


def for_ward():
    img("add")


def back_ward():
    img("sub")


def img(string):
    global image_area
    global image
    global paths
    global i
    global status
    image_area.grid_forget()
    status.grid_forget()
    if string == "sub":
        i -= 1
    elif string == "add":
        i += 1
    if i < 0:
        i = len(paths)-1
    elif i == len(paths):
        i = 0
    image = Image.open(paths[i])
    x, y = image.size
    if x > 800:
        x = x//3
        y = y//3
    image = ImageTk.PhotoImage(image.resize((x, y), Image.ANTIALIAS))
    image_area = tk.Label(root, image=image, justify="center")
    image_area.grid(column=0, row=0, columnspan=3)
    name = get_name(paths[i])
    status = tk.Label(
        root, text=f"image name : {name}", anchor=E, relief=SUNKEN, bd=1)
    status.grid(row=2, columnspan=3, sticky=W+E)


file = filedialog.askopenfilename(
    initialdir="/", filetypes=[("jpg", "*.jpg")])

paths = get_list(get_path(file))
i = paths.index(file)
image = Image.open(paths[i])
x, y = image.size
if x > 800:
    x = x//3
    y = y//3

image = ImageTk.PhotoImage(image.resize((x, y), Image.ANTIALIAS))
image_area = tk.Label(root, image=image)
image_area.grid(column=0, row=0, columnspan=3)

# Buttons(exit,farward,backward)
exit = tk.Button(root, text="Exit", command=root.quit)
forward = tk.Button(root, text=">>", command=lambda: for_ward())
backward = tk.Button(root, text="<<", command=lambda: back_ward())

# button placing
exit.grid(row=1, column=1, pady=10)
forward.grid(row=1, column=2)
backward.grid(row=1, column=0)


def get_name(string):
    name = string.split("/")
    return name[len(name)-1]


name = get_name(paths[i])
status = tk.Label(root, text=f"image name : {name}", anchor=E, relief=SUNKEN)
status.grid(row=2, columnspan=3, sticky=W+E)

# status

root.mainloop()
