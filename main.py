from bs4 import BeautifulSoup
import requests

search = input("Enter search here: ")
param = {"q" : search}

r= requests.get("https://www.bing.com/search?", params=param)

soup = BeautifulSoup(r.text, "lxml")
results = soup.find("ol", {"id" : "b_results"})
links = results.findAll("li", {"class" : "b_algo"})
##print(soup.prettify())

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs['href']
    ##item_des = item.find("p").text
    if item_text and item_href:
        print(item_text)
        print(item_href, "\n")

    children = list(item.children)[0]
    print("Next Sibling :", children.next_sibling)