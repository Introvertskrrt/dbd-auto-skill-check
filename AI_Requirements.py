import os
import time
import wget
import zipfile
import gdown

def downloader():
    if os.path.exists(r"AI_Resources\Tesseract-OCR\tesseract.exe"):
        return
    else:
        directory = os.getcwd()
        path = os.path.abspath(directory)

        print("It looks like this is your first time using this program!\nWe will download some resources for the AI first :D")
        print("Download is in progress...\n")
        URL = "https://drive.google.com/u/1/uc?id=1ANMFDDDoZNQRPJS-voOAXsN6KchRX23H"
        gdown.download(URL, "AI_Resources.zip", quiet=False)
        time.sleep(2)

        zip_path = f"{path}\\AI_Resources.zip"
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(f"{path}\\")
            print("\nStarting...")
            time.sleep(2)
        os.remove("AI_Resources.zip")

