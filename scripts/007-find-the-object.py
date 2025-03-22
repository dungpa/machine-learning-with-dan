from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key_007
from tkinter import Tk, messagebox

#IMPORTANT: THIS AI IS BROKEN SO WE HAVE NOT MADE ANY PROGRESS ON IT.
# treat this key like a password and keep it secret!
key = api_key_007

root = Tk()
root.withdraw()

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("first.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
messagebox.showinfo("Test:", "I think this is '%s' and I believe this with %d%% confidence" % (label, confidence))