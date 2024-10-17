import requests
import ctypes
import os
import tempfile
import time
from pathlib import Path

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def change_wallpaper(image_path):
    return ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def set_wallpaper_with_retry(image_path, max_retries=10, delay=2):
    for attempt in range(max_retries):
        success = change_wallpaper(image_path)
        if success:
            print("Wallpaper changed successfully!")
            return True
        else:
            print(f"Attempt {attempt + 1}/{max_retries} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Failed to change the wallpaper after multiple attempts.")
    return False

image_url = "https://i0.wp.com/picjumbo.com/wp-content/uploads/anonymous-hacker-free-photo.jpg?w=2210&quality=70"

with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
    temp_path = temp_file.name

def Wallpaper():
    download_image(image_url, temp_path)
    set_wallpaper_with_retry(temp_path)
    os.remove(temp_path)
