import tkinter as tk
import cv2
import time
from PIL import Image, ImageTk
import random

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
            remark = random.choice(negative_remarks)
            countdown_label.config(text=remark)
            capture_screenshot()
    
    # Start the countdown from 3 seconds
    countdown(3)

def capture_screenshot():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return
    
    # Read a frame from the webcam
    for i in range(0, 10):
        ret, frame = cap.read()
    
    # Release the webcam
    cap.release()
    
    # Check if the frame was captured successfully
    if ret:
        # Save the captured frame as an image file
        timestamp = int(time.time())
        filename = f"img/screenshot_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved as {filename}")
        display_image(filename)
    else:
        print("Error: Could not capture a frame from the webcam.")

def display_image(filename):
    # Load the captured image using Pillow (PIL)
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    
    # Create a label to display the image
    global image_label
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack()
    
    root.after(5000, show_start_screen)

def show_start_screen():
    countdown_label.pack_forget()
    text_label.pack(pady=20)
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
text_label.pack(pady=20)

button = tk.Button(root, text="Gib Foto!", command=button_click, font=("Helvetica", 32))
button.pack()

countdown_label = tk.Label(root, font=("Helvetica", 48))

image_label = None

root.update_idletasks()
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
text_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

root.mainloop()
