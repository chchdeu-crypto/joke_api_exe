import requests
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming"
    params = {"blacklistFlags": "nsfw,religious,political,racist,sexist,explicit","type": "single","safe-mode": ""}
    response = requests.get(url,params=params)
    data=response.json()
    return data

def is_safe_joke(joke_data):
    if joke_data["error"]==False:
        return False
    if joke_data["type"]!="single":
        return False
    if len(joke_data['joke'])==0:
        return False
    if joke_data["flags"]['nsfw']!=False and joke_data["flags"]['religious']!=False and joke_data["flags"]['political']!=False and joke_data["flags"]['racist']!=False and joke_data["flags"]['sexist']!=False and joke_data["flags"]['explicit']!=False:
        return False
    return True