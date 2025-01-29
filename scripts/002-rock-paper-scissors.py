from mlforkidsimages import MLforKidsImageProject
from authorisation import api_key_002

#Note: This AI is very dumb.

key = api_key_002

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("rock.png")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print ("You used: '%s' with %d%% confidence" % (label, confidence))