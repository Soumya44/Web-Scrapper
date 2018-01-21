from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
from io import BytesIO

def Image_Scrap():
    # Limit Specifier
    limit = 4

    # Terminating Keywords
    terminate = ["quit", "exit", "stop", "EXIT", "QUIT", "Exit", "Quit", "STOP", "Stop", "Terminate", "terminate", "TERMINATE"]

    print('Type "quit" or "exit" to EXIT')

    search = input("Enter Search Keyword :")

    # Termination Check
    if search in terminate:
        exit(0)

    dir_name = search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs("./Image_Results/"+dir_name+"/")

    param = {"q": search}

    r = requests.get("https://www.bing.com/images/search", params=param)

    soup = BeautifulSoup(r.text,"html.parser")

    results = soup.select("a.thumb")

    for item in results:

        if limit == 0:
            break

        try:
            img_obj = requests.get(item.attrs["href"])
            img_title = item.attrs["href"].split("/")[-1]
            print("Getting : "+item.attrs["href"])
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./Image_Results/"+dir_name+"/"+img_title)
                limit -= 1
            except:
                print("Couldn't Save Image !!!")
        except:
            print("Error In Operation !!!")

Image_Scrap()
