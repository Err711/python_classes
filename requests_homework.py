import requests
import pprint
import json


class ImgDownload:
    def __init__(self, url):
        self.response = None
        self.url = url

    def download_image(self):
        with open(f"new_photo.png", "wb") as photo:
            try:
                self.response = requests.get(self.url)
            except Exception as err:
                print(f"smth happened {err}")
            if self.response.status_code == 200:
                photo.write(self.response.content)
                print(f"image from {self.url} is downloaded")


a = ImgDownload(input("Enter img link: \n"))
print(a.download_image())
