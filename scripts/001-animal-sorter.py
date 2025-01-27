from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key
from tkinter import Tk, messagebox, Label
from PIL import Image, ImageTk

key = api_key

root = Tk()
image_path = "alligator.jpg"
image = Image.open(image_path)
image = image.resize((500, 500), Image.Resampling.LANCZOS)  # Resize image to fit the window
tk_image = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
image_label = Label(root, image=tk_image)
image_label.pack(pady=10)

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("alligator.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
messagebox.showinfo("The results are:", "I think it is closest to the: '%s' with %d%% confidence" % (label, confidence))

root.mainloop()