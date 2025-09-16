import os
import ctypes
from tkinter import *
from PIL import Image, ImageTk
from pytube import Playlist
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog, ttk
import subprocess
import threading
import psutil


font_path = os.path.abspath("KronaOne-Regular.ttf")
ctypes.windll.gdi32.AddFontResourceW(font_path)





#THEMES
dark_theme = {
    "bg": "#1C222E",
    "entry_bg": "#1A1A1A",
    "text": "white",
    "button_bg": "#1A1A1A",
    "accent": "#4C566A"
}

light_theme = {
    "bg": "#F9F9F9",          
    "entry_bg": "#1A1A1A",    
    "text": "#2D2D2D",        
    "button_bg": "#1A1A1A",   
    "accent": "#B8BCC2"        
}

current_theme = dark_theme


#Funtions


def toggle_theme():
     global current_theme

     if current_theme == dark_theme:
          current_theme  = light_theme
     else:
          current_theme = dark_theme



     apply_theme()


def apply_theme():
     window.config(bg=current_theme["bg"])
     title_text.config(bg=current_theme["bg"], fg=current_theme["text"])
     text_2.config(bg=current_theme["bg"], fg=current_theme["text"])
     entry.config(bg=current_theme["bg"])
     actual_entry.config(bg=current_theme["entry_bg"], fg="White")
     paste_button.config(bg=current_theme["button_bg"], activebackground=current_theme["button_bg"])
     start_button.config(bg=current_theme["bg"], activebackground=current_theme["bg"])
     progress_box.config(bg=current_theme["bg"])
     theme_button.config(bg=current_theme["bg"], activebackground=current_theme["bg"])
     

def paste_url():
       clipborard_text = window.clipboard_get()
       actual_entry.delete(0,END)
       actual_entry.insert(0, clipborard_text)

       pasted_img = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\Group 1 (1).png")
       pasted = Label(window, image=pasted_img, bg='#1A1A1A', bd=0)
       pasted.image = pasted_img  
       pasted.place(x=400,y=170) 
       window.after(1500, pasted.destroy)





download_process = None

          




import threading

def start_download():
    def run_download():
        try:
            url = actual_entry.get()
            directory = filedialog.askdirectory()
            if not directory:
                return

            # Progress label
            progress_label = Label(window, text="Downloading...", font=("Krona One", 12), fg='white', bg='#2C2C2C')
            progress_label.place(x=80, y=350)
            window.update_idletasks()

            yt_dlp_path = "C:\\Users\\LENOVO\\Downloads\\yt-dlp.exe"
            ffmpeg_path = "C:\\Users\\LENOVO\\Downloads"

            env = os.environ.copy()
            env["PATH"] = ffmpeg_path + os.pathsep + env["PATH"]

            command = [
                yt_dlp_path,
                '--extract-audio',
                '--audio-format', 'mp3',
                '--yes-playlist',
                '-o', os.path.join(directory, '%(title)s.%(ext)s'),
                url
            ]

            global download_process
            download_process  =  subprocess.Popen(command, env=env)
            download_process.wait()
            
            if download_process.returncode == 0:
                 progress_label.config(text="Download Complete!")
                 messagebox.showinfo("Download Complete", f"MP3 files saved to:\n{directory}")


            else:
                 progress_label.config(text="Download Cancelled.")
                 
                 
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    threading.Thread(target=run_download).start()




def cancel_dowmload():
     global download_process
     if download_process and download_process.poll() is None:
          
          parent = psutil.Process(download_process.pid)
          for child in parent.children(recursive=True):
               
             child.kill()
             parent.kill()


          download_process.terminate()
          messagebox.showinfo("Cancelled", "Download has been cancelled.")
          

#Setup
window = Tk()
window.title("Snip Tube")
window.geometry("600x600")
window.config(bg='#1C222E')
window.iconbitmap("C:\\Users\\LENOVO\\Downloads\\favicon.ico")


#Main text 
title_text = Label(window, text="SNIP TUBE", font=("Krona One", 20) ,fg='White', bg='#1C222E')
title_text.place(x=200,y=20)

#Text 2
text_2 = Label(window, text="Paste Your URL here", font=("Krona One", 16), fg='White', bg='#1C222E')
text_2.place(x=76,y=110)


#Entry box 
entry_img = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\entry box new.png")
entry = Label(window, image=entry_img , bg='#1C222E')
entry.place(x=61,y=150)

actual_entry = Entry(window, width=25, font=('Krona One', 12),  fg='White', bg='#1A1A1A', bd=0)
actual_entry.place(x=90,y=178)



#Paste button
paste_img  = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\Vector.png")
paste_button = Button(window, image=paste_img,  fg='White', bg='#1A1A1A', bd=0, activebackground='#1A1A1A',highlightthickness=0, command=paste_url)
paste_button.place(x=426,y=170)

 
pasted_img = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\Group 1.png")

#Start button
start_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\YT Playlist Snacher\\assets\\download button.png")
start_button = Button(window , image=start_img, fg='White', bg='#1C222E', bd=0 , activebackground='#1C222E', command=start_download)
start_button.place(x=61,y=241)

#Progress box
progress_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\YT Playlist Snacher\\assets\\progress box.png")
progress_box = Label(window, image=progress_img, fg='White', bg='#1C222E', bd=0 , activebackground='#1C222E' )
progress_box.place(x=61,y=332)

#Cancel button
cancel_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\YT Playlist Snacher\\assets\\cancel.png")
cancel_button = Button(window, image=cancel_img,   fg='White', bg='#2C2C2C', bd=0, activebackground='#2C2C2C',highlightthickness=0, command=cancel_dowmload)
cancel_button.place(x=415,y=349)




#DARK/LIGHT
theme_img = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\day-and-night.png")
theme_button = Button(window, image=theme_img,bg='#1C222E',bd=0, activebackground='#1C222E' , command=toggle_theme)
theme_button.place(x=23,y=22)




window.mainloop()