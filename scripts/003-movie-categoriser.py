from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key_003
from tkinter import Tk, messagebox, Label
from PIL import Image, ImageTk

# treat this key like a password and keep it secret!
key = api_key_003

def get_response():
    you = input("What genre do you think it is? Action, family or drama? (Do not start with uppercase.) ")
    return you

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("dragonprince.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

root = Tk()
image_path = "dragonprince.jpg"
image = Image.open(image_path)
image = image.resize((500, 500), Image.Resampling.LANCZOS)  # Resize image to fit the window
tk_image = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
image_label = Label(root, image=tk_image)
image_label.pack(pady=10)

your_response = get_response()

# CHANGE THIS to do something different with the result
messagebox.showinfo("Result", "I think it is a: '%s' movie with %d%% confidence." % (label, confidence))

if your_response == label:
    messagebox.showinfo("What I think:", "I agree with you on what genre it is.")
else:
    messagebox.showinfo("What I think:", "I'm not sure if you are thinking of the right genre.")

