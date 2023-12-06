import os
import gdown

file_url = "https://drive.google.com/uc?export=download&id=1p_DrK0w5SYebJ21scnyNdjV1Fr8-sdUx"
file_name = "best.pt"

# Check if the file already exists in the directory
if not os.path.exists(file_name):
    # If the file doesn't exist, download it using gdown
    gdown.download(file_url, file_name, quiet=False)
    print(f"{file_name} downloaded successfully.")
else:
    print(f"{file_name} already exists in the directory. No need to download.")
