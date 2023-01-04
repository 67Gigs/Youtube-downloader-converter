import tkinter as tk
from tkinter import ttk
from ctypes import windll
from pytube import YouTube as ytb
from moviepy.editor import *



def alert(str):
    alert = tk.Tk()
    alert.title("Done!")
    alert.geometry("200x100")
    alert.resizable(False, False)
    text = ttk.Label(alert, text=str)
    text.pack()
    b_exit = tk.Button(alert, text="Exit", command=lambda: alert.quit())
    b_exit.pack()
    alert.mainloop()


def converter(str):
    alert('Converting...')
    try:
        yt = ytb(str)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename=yt.title+'.mp3')
        alert("Done!")        
    except:
        alert("Error!")
        
        
def downloader(str):
    yt = ytb(str)
    try:
        stream = yt.streams.get_by_itag(yt.streams.get_highest_resolution().itag)
        stream.download(filename=yt.title+'.mp4')
        alert("Done!")
    except:
        alert('Error!')

root = tk.Tk()
root.title("YouTube Downloader and Converter")

window_width = 500
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

# root.minsize(600, 400)
# root.maxsize(1920, 1080)

# root.attributes('-alpha', 1)
# root.attributes('-background', 'black')
# root.attributes('-topmost', 1)

root.iconbitmap('C:\\Users\\noure\\Desktop\\Etudes\\python\\png-to-ico\\logo.ico')
text = ttk.Entry(root, width=50)

text.pack()

b_download = tk.Button(root, text="Download video", command=lambda: downloader(text.get()))
b_download.pack()


b_convert = tk.Button(root, text="Convert video", command=lambda: converter(text.get()))
b_convert.pack()

b_exit = tk.Button(root, text="Exit", command=lambda: root.quit())
b_exit.pack()


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()