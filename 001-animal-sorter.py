from mlforkidsimages import MLforKidsImageProject
from tkinter import Tk, messagebox

# treat this key like a password and keep it secret!
key = "c0e76be0-d9b3-11ef-83aa-75c08270f6280d1b2cc1-7ed4-436a-a0f0-ee317f08e381"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("alligator.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

root = Tk()
root.withdraw()

# CHANGE THIS to do something different with the result
messagebox.showinfo("The results are:", "I think it is closest to the: '%s' with %d%% confidence" % (label, confidence))

