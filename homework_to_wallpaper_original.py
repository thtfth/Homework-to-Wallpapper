from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import time
import ctypes

list_of_work = {}

user_name = os.getlogin()


#script_dir = os.path.dirname(file_loc) #<-- absolute dir the script is in
#rel_path = "/works.png"
#abs_file_path = os.path.join(script_dir, rel_path)

print("WARNING: THIS PROGRAM WILL CHANGE YOUR WALLPAPER INSTATLY AFTER IT'S FINISHED. PLS REMEMBER TO RECORD THE OLD WALLPAPER FILE LOCATION")

def text_to_image(text):
    def getSize(txt, font):
        testImg = Image.new('RGB', (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)

    if __name__ == '__main__':

        fontname = "arial.ttf"
        fontsize = 30

        colorText = "black"
        colorOutline = "white"
        colorBackground = "white"


        font = ImageFont.truetype(fontname, fontsize)
        width, height = getSize(text, font)
        img = Image.new('RGB', (width+1920, height+1080), colorBackground)
        d = ImageDraw.Draw(img)
        d.text((750, height/2), text, fill=colorText, font=font)
        d.rectangle((0, 0, width+1920, height+1080), outline=colorOutline)

        img.save(file_loc)

#omg that part is finally done.

def personality():
    personality = input('This is just a funny question: Are you a funny person? y/n')

    if personality == 'y':
        print('ok guess u r a funny person. YaY')
        return 'y'
    elif personality == 'yes':
        print('...i told you to answer with y or n and you answered yes... I guess u r a funny person then! :)')
        return 'y'
    elif personality == 'n':
        print('Sorry for that ridiculous quesion. Here is the code:')
        return 'n'
    elif personality == 'no':
        print('...i told you to answer with y or n and you answered no... I guess u r a funny person then! :)')
        return 'y'

#here is the code for NOT funny person

def ur_homework():
    #subject_abbr = {'Social Studies' : 'sos', 'French' : 'fre', 'Technology' : 'tec', 'Science' : 'sci', 'Math' : 'mat', 'Christian Education' : 'ce', 'English' : 'eng'}
    subject_q = str(input('Subject: '))

    detail = str(input('Detail: '))

    list_of_work[subject_q] = detail

    more = str(input('Do u have more? y/n: '))

    if more == 'y':
        #print('k, gald to hear that! *evil laugh*')
        #print(list_of_work)
        ur_homework()

    elif more == 'yes':
        #print('...i told you to answer with y or n and you answered yes... I guess u have more stuff then! :)')
        #print(list_of_work)
        ur_homework()

    elif more == 'n':
        #print('Ok then, pls check ur wallpaper!')
        #print('Please check your wallpaper.')
        #print(list_of_work)
        return list_of_work

    elif more == 'no':
        #print('...i told you to answer with y or n and you answered no... Too bad...')
        #print('Please check your wallpaper.')
        #print(list_of_work)
        return list_of_work

def dic_to_text(works):

    with open(txt_file_loc, 'w') as f:
        for title, detail in works.items():
            f.write(f'{title.upper()}:\n{detail}\n\n')


    with open(txt_file_loc, 'r') as f:
        pass
        #print(f.read())


#using defs



file_loc_folder = input(f'Homework image file storage location (Leave blank if want it by default location: C:\\Users\\{user_name}\\Desktop\\Homeworks): ')

if file_loc_folder == '':
    file_loc_folder = r"C:\Users" + "\\" + user_name + "\\" + r"Desktop\Homeworks"

txt_file_loc = file_loc_folder + '\\homeworks.txt'

if not os.path.exists(file_loc_folder):
    os.makedirs(file_loc_folder)

if __name__ == '__main__':

    file_loc = file_loc_folder + '\\' + 'homeworks.png'

    print(file_loc_folder)

    ur_homework()

    dic_to_text(list_of_work)

    homeworks = open(txt_file_loc, 'r')

    text_to_image(homeworks.read())

    print("Please check your wallpaper!")

    print("Press ctrl c to quit the program :)")

    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_loc , 0)

    time.sleep(100000)
