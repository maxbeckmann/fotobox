import tkinter as tk
import cv2
import time
from PIL import Image, ImageTk
import random
from sony import CameraHandler

negative_remarks = [
    "Das ist schrecklich!",
    "Was für eine Katastrophe!",
    "Das sieht schrecklich aus!",
    "Absolut furchtbar!",
    "Ich kann es nicht glauben...",
    "Das ist so schlecht!",
    "Unglaublich schlecht!",
    "Nicht gut!",
    "Schlechte Qualität!",
    "Völlig enttäuschend!",
    "Das ist inakzeptabel!",
    "Ich habe Besseres erwartet...",
    "Enttäuschend!",
    "Sehr enttäuschend!",
    "Könnte besser sein...",
    "Ich bin nicht beeindruckt...",
    "Das ist einfach schlecht...",
    "Absolut schrecklich!",
    "Ich bin nicht zufrieden...",
    "Eine totale Enttäuschung!"
]


def button_click():
    # Hide the current widgets
    print(text_label)
    text_label.pack_forget()
    button.pack_forget()
    
    # Create a label for countdown
    countdown_label.pack(pady=100)
    
    # Define a countdown function
    def countdown(count):
        if count > 0:
            countdown_label.config(text=str(count))
            root.after(1000, countdown, count - 1)  # Update countdown every 1000 ms (1 second)
        else:
            success = take_picture()
            if success:
                countdown_label.pack_forget()
            else:
                root.after(500, show_start_screen)
    
    # Start the countdown from 3 seconds
    countdown(3)

def take_picture():
    c = CameraHandler()
    img = c.get_one_picture()
    if img:
        display_image(img)
        return True
    return False

def display_image(image):
    aspect_ratio = 4/3
    width = 1200
    height = int(width / aspect_ratio)
    maxsize = (width, height)
    image.thumbnail(maxsize)
    # Load the captured image using Pillow (PIL)
    photo = ImageTk.PhotoImage(image)
    
    # Create a label to display the image
    global image_label
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack()
    
    root.after(5000, show_start_screen)

def show_start_screen():
    countdown_label.pack_forget()
    text_label.pack(pady=10)
    button.pack()
    
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    text_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    
    if image_label:
        image_label.photo = None
        image_label.destroy()
    else:
        print("fuck")


root = tk.Tk()
root.attributes('-fullscreen', True)

text_label = tk.Label(root, text="Fotobox bereit", font=("Helvetica", 24))
text_label.pack(pady=10)

button = tk.Button(root, text="Gib Foto!", command=button_click, font=("Helvetica", 32))
button.pack()

countdown_label = tk.Label(root, font=("Helvetica", 48))

image_label = None

root.update_idletasks()
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
text_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

root.mainloop()
