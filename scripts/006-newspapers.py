import requests
from authorisation import api_key_006
from tkinter import messagebox, Tk, Canvas, NORMAL, HIDDEN

headlines = ["REUSABLE BAGS IN ENGLAND", "BEAVERS RELEASED FROM SANCTUARY", "SAND TIGER SHARK BORN IN AQUARIUM DISCOVERY", "BLOOMING SEASON FOR FLOWERS", "FIRST ANIMAL BORN IN SEA LIFE", 
"BUMFRESH CATASTROPHE", "BOTTOMS TURN PURPLE", "BILLIONARE IS IN FOR A DISASTER OF BUMFRESH", "DESTRUCTION OF BUMFRESH", "HORROR OF PURPLE BOTTOMS"]

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = api_key_006
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
root = Tk()
c = Canvas(root, width=400, height=500)
c.configure(bg='deep sky blue', highlightthickness=0)
c.body_color = 'yellow'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=NORMAL)

c.pack()

for headline in headlines:
    # CHANGE THIS to something you want your machine learning model to classify
    demo = classify(headline)

    label = demo["class_name"]
    confidence = demo["confidence"]
    
    print(headline)

    # CHANGE THIS to do something different with the result
    messagebox.showinfo("Opinion", "I think this newspaper headline is '%s' and I believe this with %d%% confidence" % (label, confidence))