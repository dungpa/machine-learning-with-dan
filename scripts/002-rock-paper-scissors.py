from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key_002
from tkinter import Tk, messagebox
from random import randint

key = api_key_002

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("rock.png")

label = demo["class_name"]
confidence = demo["confidence"]

root = Tk()
root.withdraw()

# CHANGE THIS to do something different with the result
messagebox.showinfo("What your move was:", "You used: '%s' with %d%% confidence" % (label, confidence))

airesult = randint(1, 4)

aiwin = False

ailose = False

aidraw = False

if airesult == 1:
    aiwin = True
elif airesult == 2:
    ailose = True
else:
    aidraw = True
    
if aiwin == True and label == 'Rock':
    messagebox.showinfo("The results:", "I used Paper and won.")
elif aiwin == True and label == 'Paper':
    messagebox.showinfo("The results:", "I used Scissors and won.")
elif aiwin == True and label == 'Scissors':
    messagebox.showinfo("The results:", "I used Rock and won.")  

if ailose == True:
    messagebox.showinfo("You win.", "You have beaten me.")
    
