# Import needed libraries
import ctypes
import subprocess
import sys
import os
import time

print('Attempting to install needed libraries for this script...')
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'Pillow'])
except:
    print('------------------------------------------------------------------------------------------------------\nERROR: Could not install the need pip dictionaries. Please check your pip installation\n------------------------------------------------------------------------------------------------------')

# Import needed libraries from pip
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Create a list for works. (Useless when using the txt to wallpaper version)
list_of_work = {}

# Find the windows username
user_name = os.getlogin()

# Warn the user that this program will replace their current wallpaper
print("------------------------------------------------------------------------------------------------------\nWARNING: THIS PROGRAM WILL CHANGE YOUR WALLPAPER INSTATLY AFTER IT'S FINISHED. PLS REMEMBER TO RECORD THE OLD WALLPAPER FILE LOCATION\n------------------------------------------------------------------------------------------------------")

# COPYRIGHT TO LEO YU
print("Copyright to Leo Yu\n")

# Credit to a Stackoverflow user. (Forgot to link source :( )
# Convert a text file to a .png
def textToImage(SaveFileLoc, text, size):
    def getSize(txt, font):
        testImg = Image.new('RGB', (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)

    if __name__ == '__main__':

        fontname = "arial.ttf"
        fontsize = size

        colorText = "black"
        colorOutline = "white"
        colorBackground = "white"


        font = ImageFont.truetype(fontname, fontsize)
        width, height = getSize(text, font)
        img = Image.new('RGB', (width+1920, height+1080), colorBackground)
        d = ImageDraw.Draw(img)
        d.text((900, height/2), text, fill=colorText, font=font)
        d.rectangle((0, 0, width+1920, height+1080), outline=colorOutline)

        img.save(SaveFileLoc)


# Also from the internet. Used to kill Steam Wallpaper Engine
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


# Ask for the file location to store the text and image files
# Default to desktop (without folder)
def getFileLoc():
    global image_loc
    global txt_file_loc

    # Ask for file location input
    desktopOrFolder = input(f'Do you want your text and image file saved on the Desktop(y, Default) or in a separate folder(n)? y/n:')
    if desktopOrFolder == 'y' or 'yes':
        file_loc_folder = input(f'Homework image file storage location (Leave blank if want it by default location: C:\\Users\\{user_name}\\Desktop): ')
        if file_loc_folder == '':
            file_loc_folder = r'C:\Users' + '\\' + user_name + '\\' + r'Desktop'
    else:
        file_loc_folder = input(f'Homework image file storage location (Leave blank if want it by default location: C:\\Users\\{user_name}\\Desktop\\Homeworks): ')      
        if file_loc_folder == '':
            file_loc_folder = r'C:\Users' + '\\' + user_name + '\\' + r'Desktop\Homeworks'

    # Makes path if the path doesn't exist
    if not os.path.exists(file_loc_folder):
        os.makedirs(file_loc_folder)

    # Get text file location
    txt_file_loc = file_loc_folder + '\\homeworks.txt'

    # Makes homework.txt if does's exist
    if not os.path.exists(txt_file_loc):
        f = open(f'{txt_file_loc}', 'x')
        f.close()

    # Get image file location
    image_loc = file_loc_folder + '\\' + 'homeworks.png'
    
    # Print the file for user to see where the files are
    print(file_loc_folder)



# Ask for custom font size
def getFontSize():
    global fontSize

    # Get input from user
    fontSize = input('Font Size (Default 30): ')

    # Default fontsize to 30 the input is empty
    if fontSize == '':
        fontSize = int(30)
    else:
        fontSize = int(fontSize)


# Ask for custom font (WORK IN PROGRESS)
def getFontFamily():
    pass


if __name__ == '__main__':
    # Ask and get for file storage location
    getFileLoc()

    # Ask for font size
    getFontSize()

    # Check if steam wallpaper engine is running. If so, terminates it so the wallpaper generated can display properly.
    if process_exists('wallpaper32.exe') == True:
        # Kill 32bits version of steam wallpaper engine
        print('Steam Wallpaper engine (32 bits) is running! Terminating program...')
        os.system("taskkill /f /im  wallpaper32.exe")
    elif process_exists('wallpaper64.exe') == True:
        # Kill 64bits version of steam wallpaper engine
        print('Steam Wallpaper engine (64 bits) is running! Terminating program...')
        os.system("taskkill /f /im  wallpaper64.exe")

    # Initiate for file display
    fileRead = open(txt_file_loc)

    # Display the file
    f = fileRead.read()
    print('--------------------------------------------------------------------------')
    print(f)
    print('--------------------------------------------------------------------------')
    f.close()
    
    # Display image file location
    print(image_loc)

    # Generate image
    textToImage(image_loc, f, fontSize)

    # Inform process has been done
    print('Done')

    # Changes the wallpaper automatically
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_loc , 0)

    # Automatically shuts down
    time.sleep(5)