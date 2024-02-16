import requests
import sys
from bs4 import BeautifulSoup
import requests
import pyautogui
import os

def downloadWallpaper(link):
    pageLink = link
    end = ""
    start = "https://images" + ".alphacoders.com/"

    for i in range(2,10,1):
        if(pageLink.startswith("https://wall.alphacoders.com")):
            imgLink = start + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "")[0:3] + "/" + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "") + ".png"
            r = requests.get(imgLink)
            end = ".png"
            if(r == "<Response [403]>" or r.status_code == 404):
                imgLink = start + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "")[0:3] + "/" + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "") + ".jpeg"
                r = requests.get(imgLink)
                end = ".jpeg"
                if(r == "<Response [403]>" or r.status_code == 404):
                    imgLink = start + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "")[0:3] + "/" + pageLink.replace("https://wall.alphacoders.com/big.php?i=", "") + ".jpg"
                    r = requests.get(imgLink)
                    end = ".jpg"
                    if(r == "<Response [403]>" or r.status_code == 404):
                        pass
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            print(imgLink, r.content)
            break
        start = "https://images" + str(i) + ".alphacoders.com/"


    with open("wallpaper.png", "wb") as f:
        f.write(r.content)
    f.close()

def grabLink():
    url = 'https://desktoptinkerer.onrender.com/link' 
    response = requests.get(url)
    stored_link = ""
    if response.status_code == 200:
        print(response.json())
        stored_link = response.json()['Saved link']
        print("Stored link:", stored_link)
    else:
        print("Failed to retrieve link:", response.text)
    return stored_link

def screenShotWallpaper():
    screenshot = pyautogui.screenshot()

    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

def uploadWallpaper():
    upload_url = 'https://desktoptinkerer.onrender.com/upload_png'

    predefined_key = "jsjsjfuefihiuhsjfdshfuefhuhjdsfahuedioadsijwkjkljfkjsdioujiopureiopqwuiorgsdmnmbshuifynbcfgidsahiudhfasdh"

    files = {'file': open('screenshot.png', 'rb')}
    data = {'signature': predefined_key}

    response = requests.post(upload_url, files=files, data=data)

    if response.status_code == 200:
        print("Screenshot uploaded successfully.")
    else:
        print("Failed to upload screenshot.")
        print("Response:", response.text)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit()

    command = sys.argv[1]
    if(command == "download"):
        link = grabLink()
        downloadWallpaper(link)
    if(command == "upload"):
        uploadWallpaper()
    if(command == "ss"):
        screenShotWallpaper()