# Picture -> GIF

This is a tool for people who have a collection of images that are too large to be passed through a website and converted to a gif - no matter the size of the collection, this can create you a gif from them.

## Pre-Requirements
Install the latest version from the [releases](https://github.com/N4GR/Picture-To-GIF/releases) category, make sure to install the appropriate version depending on your operating system.
> [!NOTE]
> If running the run.bat or run.sh file doesn't install the correct dependencies, launch your command prompt from the folder you installed the program and run the line of code below.
```bash
pip install -r "requirements.txt"
```

## Usage/Examples
- Put images in the images folder
- Run the script with the run.sh or run.bat
- Wait for the script to ask for a time in between images and then type in your time
- Wait for the program to convert and you should see the gif in the gifs folder

> [!NOTE]
> If the batch or shell script doesn't launch correctly, open your command prompt in the folder you downloaded the script and run the below command.
```bash
python ./main.py
```


## FAQ

#### x format doesn't work with this program!

If a particular format doesn't work with the program, please create an [issue](https://github.com/N4GR/Picture-To-GIF/issues) ticket with the enhancement tag listing the desired format.

#### Do you plan on making this script convert other files?

At the moment there are plans on creating a larger program for multiple other formats, but this repo will be dedicated towards images to gifs.

## Support
For support, create an issues ticket.

[![Festival](https://img.shields.io/badge/GitHub-N4GR-blue?style=for-the-badge&logo=github&labelColor=red&color=white)](https://github.com/N4GR)

> [!WARNING]
> GIF isn't known for its optimisation; you may experiance large file sizes for large collections of images and a large time in between frames.
