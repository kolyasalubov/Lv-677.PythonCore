"""
Python YouTube Video Downloader is an application to download videos from YouTube. This provides users to download videos they need in their devices and watch them offline. 
User has to copy the youtube video URL that they want to download and simply paste that URL in the 'Paste link here' section and click on the download button, 
it will start downloading the video. 
When video downloading finishes, it shows a message 'DOWNLOADED' popup on the window below the download button.
"""

# Install in terminal(command line) pip library pytube, tk (tkinter):
# pip install tkinter
# pip install pytube

# tkinter - standard GUI (graphical user interface) library, one of the easiest ways to build a GUI application.
# pytube - used for downloading videos from youtube

# There are below steps to perform to create a code:
# 1. Import libraries.
# 2. Create display window.
# 3. Create field to enter link.
# 4. Create function to start downloading.

# 1. Import Libraries

from tkinter import *
from pytube import YouTube 


# 2. Create Display Window

root = Tk()                                         # initializing tkinter to create Tk root widget (display window) 
                                                    # [The root widget has to be created before any other widgets and there can only be one root widget.]
root.geometry("500x300")                            # setting window’s width and height
root.resizable(0,0)                                 # setting the fix size of window, cannot change a window-Tk root widget
root.title("YouTube Video Downloader Application")  # gives a title to a window on a top 


# "Label" is a widget (function unit) which displays text that users can’t able to modify.
# It consist from "root" - is a name of a window, "text" and "font" will provide written text with appropriate font, pack organized widget in block
# pack() organizes widgets in blocks before placing them in the parent widget (root). There is expand, fill and side, we use empty as it will set as a default on a top as we need.  

Label(root, text = "YouTube Video Downloader", font ='arial 20 bold').pack()   

# 3. Create Field to Enter Link

link = StringVar()                                                                              # Holds a string where we can set text value and can retrieve it. 
                                                                                                # We can pass this variable to textvariable parameter for a widget like Entry. 
                                                                                                # The widget will automatically get updated with the new value whenever the value 
                                                                                                # of the StringVar() variable changes


Label(root, text = "Paste Link here please : ", font = "arial 15 bold ").place(x = 160, y = 60)     # Creating label with set text and font in specific position [x = 160, y = 60]
link_entry = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)                     # Entry() widget is used when we want to create an input text field, 
                                                                                                    # has a concrete place [x = 32, y = 90], width of entry widget and 
                                                                                                    # textvariable - used to retrieve the value of current text variable to the entry widget

# 4. Create Function to Start Downloading

def Downloader():
    url = YouTube(str(link.get()))                                                  # gets the youtube link from the link variable by get() and then str() will convert the link in string 
    video = url.streams.first()
    # SAVE = "C:\Users\zoria\Desktop\Python\Project Video Downloaded"                                                     # set variable video as first present stream of that video by stream.first() method
    video.download('C:/Users/zoria/Desktop/Python/Project Video Downloaded')                                                                # downloading video
    Label(root, text = "DOWNLOADED", font = "arial 15").place(x = 180, y = 210)     # informing about downloading video by widget Label in specified position. 

# 5. Create button

# Button is a widget that consist from text with its font and background color, command is used to call our created function. Botton has its own position

Button(root, text = "DOWNLOAD", font = "arial 15 bold", bg = "pale violet red", padx = 2, command = Downloader).place(x = 180, y = 150)

root.mainloop()                                                                     # root.mainloop() is a method that executes when we want to run the program.