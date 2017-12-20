from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def image_finder():
    search = input("Search for:")
    params = {"q": search}
    url="https://www.bing.com"
    r= requests.get("https://www.bing.com/images/?", params=params)
    dir_name = search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    soup = BeautifulSoup(r.text, "lxml")
    links = soup.findAll("a", {"class" : "iusc"})

    i=0
    for item in links:
        if i < 5:
            img_obj = requests.get(eval(item.attrs["m"])["murl"])
            title = (eval(item.attrs["m"]))["murl"].split("/")[-1]
            try:
                img= Image.open(BytesIO(img_obj.content))
                img.save("./"+ dir_name + "/"+ title, img.format)
                print(i)
                i += 1
            except OSError:
                continue
        else:
            break
    image_finder()


image_finder()