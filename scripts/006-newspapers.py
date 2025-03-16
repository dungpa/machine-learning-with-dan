import requests
from authorisation import api_key_006
from tkinter import messagebox, Tk

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
root.withdraw()

for headline in headlines:
    # CHANGE THIS to something you want your machine learning model to classify
    demo = classify(headline)

    label = demo["class_name"]
    confidence = demo["confidence"]
    
    print(headline)

    # CHANGE THIS to do something different with the result
    messagebox.showinfo("Opinion", "I think this newspaper headline is '%s' and I believe this with %d%% confidence" % (label, confidence))