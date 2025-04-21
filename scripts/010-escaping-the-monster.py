from mlforkidsnumbers import MLforKidsNumbers
from authorisation import api_key_010
from random import randint
from pygame import mixer
import time

#I couldn't get the chatbot to work, due to it being unable to be trained. It works very well in Scratch, though.
#Note: This AI is far dumber than its Scratch counterpart due to it constantly idling.

mixer.init()

background_music = mixer.Sound('NYEHEHEHEHE.wav')

background_music.play(loops=-1)

project = MLforKidsNumbers(
    key=api_key_010,
    modelurl="https://mlforkids-newnumbers.j8ayd8ayn23.eu-de.codeengine.appdomain.cloud/saved-models/d82a71f0-1886-11f0-86e8-690fee101d6e/status"
)

# CHANGE THIS to something you want your
# machine learning model to classify
testvalue = {
    "nano x" : 1,
    "nano y" : 1,
    "monster x" : 9,
    "monster y" : 12,
}



while True:
    response = project.classify(testvalue)
    top_match = response[0]

    label = top_match["class_name"]
    confidence = top_match["confidence"]
    nano_x = testvalue["nano x"]
    nano_y = testvalue["nano y"]
    monster_x = testvalue["monster x"]
    monster_y = testvalue["monster y"]
    # CHANGE THIS to do something different with the result
    print ("I'm at '%s' and '%s" % (nano_x, nano_y))
    if label == "go_left":
        nano_x = nano_x - 1
    elif label == "go_right":
        nano_x = nano_x + 1
    elif label == "go_up":
        nano_y = nano_y + 1
    elif label == "go_down":
        nano_y = nano_y - 1
    print ("707's at '%s' and '%s" % (monster_x, monster_y))
    strategy = randint(1, 4)
    if strategy == 1:
        if monster_y > nano_y:
           monster_y = monster_y - 1
        elif monster_x < nano_x:
           monster_x = monster_x + 1
        elif monster_x > nano_x:
           monster_x = monster_x - 1
        else:
           monster_y = monster_y + 1
    elif strategy == 2:
        if monster_y < nano_y:
           monster_y = monster_y + 1
        elif monster_x < nano_x:
           monster_x = monster_x + 1
        elif monster_x > nano_x:
           monster_x = monster_x - 1
        else:
           monster_y = monster_y - 1
    else:
        if monster_y < nano_y:
           monster_y = monster_y + 1
        elif monster_x < nano_x:
           monster_x = monster_x + 1
        elif monster_y > nano_y:
           monster_y = monster_y - 1
        else:
           monster_x = monster_x - 1
           
    nano_x = min(nano_x, 12)
    nano_x = max(nano_x, 0)
    nano_y = min(nano_y, 9)
    nano_y = max(nano_y, 0)
    monster_x = min(monster_x, 12)
    monster_x = max(monster_x, 0)
    monster_y = min(monster_y, 9)
    monster_y = max(monster_y, 0)
    
    testvalue["nano x"] = nano_x
    testvalue["nano y"] = nano_y
    testvalue["monster x"] = monster_x
    testvalue["monster y"] = monster_y
    
    if nano_x == monster_x and nano_y == monster_y:
        exit()
    
    time.sleep(1.5) 
        
        
        
