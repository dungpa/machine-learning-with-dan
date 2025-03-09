from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key_004
from tkinter import Tk, messagebox

# treat this key like a password and keep it secret!
key = api_key_004

# Note: Here is yet another dumb A.I.

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()
root = Tk()

places = ["newox.png", "NewerSO.png", "EH.jpg"]

# CHANGE THIS to the image file you want to recognize
for place in places:
    demo = myproject.prediction(place)

    label = demo["class_name"]
    confidence = demo["confidence"]
    root.withdraw()

    # CHANGE THIS to do something different with the result
    messagebox.showinfo("Next Result for '%s':" % place, "This goes to '%s'. I believe this with %d%% confidence" % (label, confidence))