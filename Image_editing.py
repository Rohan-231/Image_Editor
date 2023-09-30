from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image,ImageEnhance,ImageFilter
from tkinter import filedialog
import os

def brightness(bpos) :
    bpos = float(bpos)
    global outputImage
    enhancer =  ImageEnhance.Brightness(img)
    outputImage = enhancer.enhance(bpos)
    displayimage(outputImage)

def contrast(cpos) :
    cpos = float(cpos)
    global outputImage
    enhancer =  ImageEnhance.Contrast(img)
    outputImage = enhancer.enhance(cpos)
    displayimage(outputImage)

def sharpness(spos) :
    spos = float(spos)
    global outputImage
    enhancer =  ImageEnhance.Sharpness(img)
    outputImage = enhancer.enhance(spos)
    displayimage(outputImage)

def color(rpos) :
    rpos = float(rpos)
    global outputImage
    enhancer =  ImageEnhance.Color(img)
    outputImage = enhancer.enhance(rpos)
    displayimage(outputImage)

def displayimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage

def reset() :
    mains.destroy()
    os.open("main.py")

def rotate() :
    global img
    img = img.rotate(90)
    displayimage(img)

def changeImg() :
    global img
    imgname = filedialog.askopenfilename(title="Change Image")
    if imgname:
        img = Image.open(imgname)
        img = img.resize((600,600))
        displayimage(img)

def flip() :
    global img
    img = img.transpose((Image.FLIP_LEFT_RIGHT))
    displayimage(img)
def resize() :
    global img
    img = img.resize((200, 300))
    displayimage(img)


def crop() :
    global img
    img = img.crop((100, 100, 400, 400))
    displayimage(img)


def blur() :
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)

def emboss() :
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)

def edge() :
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)

def save() :
    global img
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)
def close():
    mains.destroy()

# Setting Main window
mains = Tk()
space=(" ")*215
screen_width = mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()

# Creating main window
mains.geometry(f"{screen_width}x{screen_height}")
mains.title(f"{space}Image Editor")
mains.configure(bg='light blue')

# <------Default image in editor------>
img = Image.open("default.jpg")
img = img.resize((700, 600))

# <------Creating panel to display image------>
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)

# Brightness Slider

bright = Scale(mains,label = "Brightness",from_=0,to=2,orient=HORIZONTAL,length=200,resolution=0.1,command=brightness,bg="PINK")
bright.set(1)
bright.configure(font=('consolas',10,'bold'),foreground='white')
bright.place(x=1070,y=15)

# Contrast Slider

constrast = Scale(mains,label = "Contrast",from_=0,to=2,orient=HORIZONTAL,length=200,resolution=0.1,command=contrast,bg="PINK")
constrast.set(1)
constrast.configure(font=('consolas',10,'bold'),foreground='white')
constrast.place(x=1070,y=90)

# Sharpness Slider

sharpness = Scale(mains,label = "Sharpneess",from_=0,to=2,orient=HORIZONTAL,length=200,resolution=0.1,command=sharpness,bg="PINK")
sharpness.set(1)
sharpness.configure(font=('consolas',10,'bold'),foreground='white')
sharpness.place(x=1070,y=165)

# Slider Button
slider = Scale(mains,label = "Colors",from_=0,to=2,orient=HORIZONTAL,length=200,command=color,resolution = 0.1,bg="yellow")
slider.set(1)
slider.configure(font=('consolas',10,'bold'),foreground='white')
slider.place(x=1070,y=240)

# Reset all the buttons
reset_button = Button(mains,text="Reset",command=reset,bg="BLACK",activebackground="ORANGE")
reset_button.configure(font=('consolas',10,'bold'),foreground='white')
reset_button.place(x=380,y=15)

# Rotate Button
rotate_button = Button(mains,text ="Rotate",command=rotate,bg="BLACK")
rotate_button.configure(font=('consolas',10,'bold'),foreground='white')
rotate_button.place(x=805,y=110)

# Change Image Button
change = Button(mains,text= "Change Image",command=changeImg,bg='BLACK',activebackground="ORANGE")
change.configure(font=('consolas',10,'bold'),foreground='white')
change.place(x=805,y=35)

# Flip Button
flip_button = Button(mains,text ="Flip",command=flip,bg="BLACK")
flip_button.configure(font=('consolas',10,'bold'),foreground='white')
flip_button.place(x=805,y=180)

# Resize Button
resize_button = Button(mains,text ="Resize",command=resize,bg="BLACK")
resize_button.configure(font=('consolas',10,'bold'),foreground='white')
resize_button.place(x=805,y=255)

# Crop Button
crop_button = Button(mains,text ="Crop",command=crop,bg="BLACK")
crop_button.configure(font=('consolas',10,'bold'),foreground='white')
crop_button.place(x=805,y=340)

# Blur Button
blur_button = Button(mains,text ="Blur",command=blur,bg="BLACK")
blur_button.configure(font=('consolas',10,'bold'),foreground='white')
blur_button.place(x=805,y=425)

# Emboss Button
emboss_button = Button(mains,text ="Emboss",command=emboss,bg="BLACK")
emboss_button.configure(font=('consolas',10,'bold'),foreground='white')
emboss_button.place(x=805,y=510)

# Edge Enhance Button
ee_button = Button(mains,text ="Edge Enhance",command=edge,bg="BLACK")
ee_button.configure(font=('consolas',10,'bold'),foreground='white')
ee_button.place(x=805,y=595)

# save Button
save_button = Button(mains,text ="Save",command=save,bg="BLACK")
save_button.configure(font=('consolas',10,'bold'),foreground='white')
save_button.place(x=805,y=675)

# Close Button
close_button = Button(mains,text ="Close",command=close,bg="BLACK")
close_button.configure(font=('consolas',10,'bold'),foreground='white')
close_button.place(x=430,y=15)


mains.mainloop()