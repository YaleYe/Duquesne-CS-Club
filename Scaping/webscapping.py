#website scapping
import requests

def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text)
    except:
        return ("ERROR")

if __name__== "__main__":
    url = "http://www.duq.edu"
    print(getHTML(url))
        
