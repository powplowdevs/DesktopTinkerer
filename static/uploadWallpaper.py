import requests
import pyautogui

screenshot = pyautogui.screenshot()

screenshot_path = "screenshot.png"
screenshot.save(screenshot_path)

upload_url = 'http://127.0.0.1:5000/upload_png'

predefined_key = "79n8y9sdyf89qo4yw78o"

files = {'file': open(screenshot_path, 'rb')}
data = {'signature': predefined_key}

response = requests.post(upload_url, files=files, data=data)

if response.status_code == 200:
    print("Screenshot uploaded successfully.")
else:
    print("Failed to upload screenshot.")
    print("Response:", response.text)
