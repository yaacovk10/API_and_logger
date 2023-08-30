import requests

def translate(word):
   
    import requests

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": "Hello, world!",
        "target": "es",
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "9010927403msh1000be5f814482fp19f61ajsn0b7f36144b09",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

translate("hello")