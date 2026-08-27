import requests
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming"
    params = {"blacklistFlags": "nsfw,religious,political,racist,sexist,explicit","type": "single","safe-mode": ""}
    response = requests.get(url,params=params)
    data=response.json()
    return data

def is_safe_joke(joke_data):
    if joke_data["error"]!=False:
        return False
    if joke_data["type"]!="single":
        return False
    if len(joke_data['joke'])==0:
        return False
    if joke_data["flags"]['nsfw']!=False and joke_data["flags"]['religious']!=False and joke_data["flags"]['political']!=False and joke_data["flags"]['racist']!=False and joke_data["flags"]['sexist']!=False and joke_data["flags"]['explicit']!=False:
        return False
    return True

def get_safe_joke():
    for _ in range(3):
        joke=get_joke()
        if is_safe_joke(joke):
            return joke
        return None

def extract_joke_data(api_data):
    joke=api_data["joke"]
    category=api_data["joke"]
    joke_id=api_data["id"]
    language=api_data["lang"]
    data={"joke":joke,"category":category,"joke_id":joke_id,"language":language}
    return data

def analyze_joke(joke):
    words=len(joke.split())
    characters=len(joke)
    return words,characters
