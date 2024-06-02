import os
import imageio.v2 as imageio
from message import logging

image_filetypes = ["jpg", "png", "jpeg", "webp", "jfif", "raw"]

def getGifID() -> int:
    return len(os.listdir("gifs/")) + 1

def getImages() -> list[str]:
    return os.listdir("images/")

def main():
    while True:
        images = getImages()
        image_count = len(images)

        if image_count == 0:
            logging.log(type = "error", text = "You haven't added any images to the images folder, add the images.")
            logging.log(type = "input", text = "Press enter to retry...")
            continue

        for image in images:
            file_type = image.split(".")[-1]
            if file_type not in image_filetypes:
                logging.log(type = "error", text = "You have a file in the images folder that isn't an image...")
                logging.log(type = "error", text = f"Please delete {image} and press enter to continue.")
                logging.log(type = "input", text = "Press enter to retry...")
                continue

        break

    logging.log(type = "note", text = f"Detected {image_count} files in the images folder...")
    
    while True:
        duration = logging.log(type = "input", text = "Enter the duration between frames (seconds): ")
        try:
            duration = int(duration)
            break
        except ValueError:
            logging.log(type = "error", text = f"You entered {duration}... This isn't a number, please enter a number and retry.")
            continue
        except:
            logging.log(type = "error", text = f"Fatal error... Stopping program.")
            exit()

    logging.log(type = "note", text = f"Beginning conversion...")
    
    ioim = []
    for filename in images:
        ioim.append(imageio.imread(f"images/{filename}"))

    gifID = getGifID()

    args = {
        "duration": duration
    }

    imageio.mimsave(f"gifs/{gifID}.gif", ioim, format = "GIF", **args)

    logging.log(type = "success", text = f"Successfully converted {image_count} images into the gif: {gifID}.gif")

if __name__ == "__main__":
    main()