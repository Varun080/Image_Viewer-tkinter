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
    """getting the path of the given 'jpg' file"""
    path = file.split("/")
    path.pop()
    path = "/".join(path)
    return path


def get_list(path):
    """getting all the files in the directory of the opened file"""
    files = []
    for i in listdir(path):
        if ".jpg" in i:
            files.append(i)
    for i in range(len(files)):
        files[i] = "/".join([path, files[i]])
    return files


def img(string):
    """while moving forword and backword chnging the image acording to the given list by 'get_list()' function and changing the lable also
        to the given file name
    """
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
    while x > 900 or y > 700:
        x = x//2
        y = y//2
    image = ImageTk.PhotoImage(image.resize((x, y), Image.ANTIALIAS))
    image_area = tk.Label(root, image=image, justify="center")
    image_area.grid(column=0, row=0, columnspan=3)
    name = get_name(paths[i])
    status = tk.Label(
        root, text=f"image name : {name}", anchor=E, relief=SUNKEN, bd=1)
    status.grid(row=2, columnspan=3, sticky=W+E)


def get_name(string):
    """info on name of the file"""
    name = string.split("/")
    return name[len(name)-1]


def right(event):
    """event binding to the right key"""
    img("add")


def left(event):
    """event binding to the left key"""
    img("sub")


# opening a browser window for browsing image (.jpg)
file = filedialog.askopenfilename(
    initialdir="/", filetypes=[("jpg", "*.jpg")])

# list of all the jpg file in the directory
paths = get_list(get_path(file))
# index of image in the path lsit
i = paths.index(file)


image = Image.open(paths[i])
# geting the size of the image
x, y = image.size
# resizing the image to be under 500x500
while x > 900 or y > 700:
    x = x//2
    y = y//2
# making the image compatible with the tkinter interface and LANCZOS image filter for better resized image quaity
image = ImageTk.PhotoImage(image.resize((x, y), Image.LANCZOS))
image_area = tk.Label(root, image=image)
# lable placing
image_area.grid(column=0, row=0, columnspan=3)

# Buttons(exit,farward,backward)
exit = tk.Button(root, text="Exit", command=root.quit)
forward = tk.Button(root, text=">>", command=lambda: img("add"))


root.bind("<Right>", right)
root.bind("<Left>", left)

backward = tk.Button(root, text="<<", command=lambda: img("sub"))

# button placing
exit.grid(row=1, column=1, pady=10)
forward.grid(row=1, column=2)
backward.grid(row=1, column=0)


# name of the file
name = get_name(paths[i])

# status bar
status = tk.Label(root, text=f"image name : {name}", anchor=E, relief=SUNKEN)
status.grid(row=2, columnspan=3, sticky=W+E)

root.mainloop()
