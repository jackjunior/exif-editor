from exif import Image
from helpers import selectFunction, clear_console
from constants import image_filename, FOLDER_PATH, MENU_OPTIONS
import enquiries, os, sys
from os import walk

def main():
    try:
        if not os.path.exists(FOLDER_PATH): 
            print("Target path does not exists!")
            input("Press enter to exit..............")
            sys.exit()
            
        filenames = next(walk(FOLDER_PATH), (None, None, []))[2]  # [] if no file

        while True:
            clear_console()
            imgList = [k for k in filenames if '.jpg' in k]
            img_filename = enquiries.choose('Please select an image to edit:', imgList)
            image_filename = img_filename
            img_path = f'{FOLDER_PATH}/{img_filename}'

            with open(img_path, 'rb') as img_file:
                img = Image(img_file)

                menu_selected = enquiries.choose('Please select function: ', MENU_OPTIONS)
                selectFunction(menu_selected, img)
    except KeyboardInterrupt:
        print("Bye! See you next time!")


if __name__ == "__main__":
    main()

        