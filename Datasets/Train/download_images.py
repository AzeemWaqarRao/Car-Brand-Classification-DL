# from bs4 import *
# import requests
# import os
# def folder_create(images):
#     folder_name = 'mercedes1'
#     os.mkdir(folder_name)
#     download_images(images, folder_name)
# def download_images(images, folder_name):
#     count = 0
#     print(f"Found {len(images)} images")
#     if len(images) != 0:
#         for i, image in enumerate(images):
#             image_link = image["src"]
#             r = requests.get(image_link).content
#             with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
#                 f.write(r)
#                 count += 1
#         if count == len(images):
#             print("All the images have been downloaded!")
#         else:
#             print(f" {count} images have been downloaded out of {len(images)}")
# def main(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     images = soup.findAll('img')
#     folder_create(images)
# url = input("Enter site URL:")
# main(url)




import requests
from bs4 import BeautifulSoup

# specify the URL of the web page you want to download images from
url = "http://www.example.com"

# send an HTTP request to the web server
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    # parse the HTML content of the web page
    soup = BeautifulSoup(response.text, "html.parser")

    # find all img tags on the page
    img_tags = soup.find_all("img")

    # create a folder to store the images
    import os
    if not os.path.exists("images"):
        os.makedirs("images")

    # iterate through the img tags and download the images
    for img in img_tags:
        img_src = img.attrs.get("src")
        if img_src.startswith("http"):
            response = requests.get(img_src)
            open(f"images/{img_src.split('/')[-1]}", "wb").write(response.content)

else:
    print("Failed to retrieve web page. HTTP Status Code:", response.status_code)
