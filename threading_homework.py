import json
import time
import requests
import os
import threading
import datetime


class Image:
    def __init__(self, name, url, path=None):
        self.name = name
        self.url = self.valid_url(url)
        self.default_path = path if path else os.getcwd()

    def valid_url(self, url):
        response = self.send_safe_request(url)

        if response.status_code == 200:
            return url
        else:
            raise ValueError("Wrong url")

    @staticmethod
    def send_safe_request(url):
        while True:
            try:
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            except Exception as err:
                raise Exception(f"Something wrong{err}")

    def download(self):
        response = self.send_safe_request(self.url)

        if response.status_code == 200:
            img_address = f"{self.default_path}/{self.name}"
            with open(img_address, "wb") as file:
                file.write(response.content)
        print("Downloaded")


class FromJsonToImg:
    def __init__(self, json_file_path):
        self.json_file_path = self.valid_path(json_file_path)
        self.image_dict = self.json_reading()
        self.image_list = self.img_creating()

    @staticmethod
    def valid_path(path):
        if not os.path.exists(path):
            raise ValueError("Wrong path")

        return path

    def json_reading(self):
        with open(self.json_file_path) as json_file:
            data = json.load(json_file)
        return data

    def img_creating(self):
        image_list = []
        for dict_ in self.image_dict:
            image_list.append(Image(name=dict_["img_name"], url=dict_["img_url"]))
        return image_list

    # def download_all_images(self):
    #     for image in self.image_list:
    #     image.download()

    def download_by_threads(self):

        thread_list = []

        for image in self.image_list:
            x = threading.Thread(target=Image.download(image), args=(image,), daemon=True)
            thread_list.append(x)
            x.start()
            time.sleep(0.1)
        b = (datetime.datetime.today() - starting_time).seconds

        print(f"it took {b} seconds")


if __name__ == "__main__":
    starting_time = datetime.datetime.today()
    json_to_image = FromJsonToImg(json_file_path="img_links_json.json")

    json_to_image.download_by_threads()
