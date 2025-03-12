import requests
from authorisation import api_key_005
from tkinter import messagebox, Tk, Canvas, NORMAL, HIDDEN

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = api_key_005
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
c.body_color = 'red'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

def insult_recieved():
    c.itemconfigure(mouth_sad, state=NORMAL)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    
def compliment_recieved():
    c.itemconfigure(mouth_sad, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=NORMAL)

c.pack()
        
while True:
    your_response = input("Give me either a compliment or an insult\n")
    
    # CHANGE THIS to something you want your machine learning model to classify
    demo = classify(your_response)

    label = demo["class_name"]
    confidence = demo["confidence"]

    # CHANGE THIS to do something different with the result
    messagebox.showinfo("My answer:", "I think you gave me: '%s' and I believe this with %d%% confidence" % (label, confidence))
    
    if label == "insults":
        insult_recieved()
    else:
        compliment_recieved()