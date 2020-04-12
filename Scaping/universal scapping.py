import requests

def geturl(url):
    try:
        r = requests.get(url,timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text)
    except:
        print("Error")

if __name__ =="__main__":
    url = "website"
    print(geturl(url))
