import requests

api_key = "VF.DM.66f95618c69ea6d002dcab91.g1iavU0zsFRnvB4P"

# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={ 'request': request },
        headers={ 
            'Authorization': api_key,
            'versionID': 'production'
        },
    )
    
    for trace in response.json():
        if trace["type"] == "text":
            print (trace["payload"]["message"])

name = input("What is your name?\n")
interact(name, {"type":"launch"})

while (True):
    nextInput = input()
    interact(name,{"type":"text","payload": nextInput})

