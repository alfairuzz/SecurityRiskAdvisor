import os
from PIL import Image


def save_architecture_image(architecture_diagram):
    # Save the uploaded image to a folder
    save_folder = "images"  # Define the folder name
    os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist

    # Define the save path
    save_path = os.path.join(save_folder, "architecture_diagram.png")

    # Save the image
    with open(save_path, "wb") as f:
        f.write(architecture_diagram.getbuffer())
        
    print("[Info] Architecture Diagram image saved.")
