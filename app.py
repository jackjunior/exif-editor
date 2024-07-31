from exif import Image
from helpers import selectFunction, clear_console
import enquiries, os, sys
from os import walk

os.system('clear')
folder_path = 'sample_images'

menu_options = [
   '1. Show Image EXIF',
   '2. Update Image Data',
   '3. Option 3',
   '4. Exit'
]

def main():
    try:
        if not os.path.exists(folder_path): 
            print("Target path does not exists!")
            input("Press enter to exit..............")
            sys.exit()
            
        filenames = next(walk(folder_path), (None, None, []))[2]  # [] if no file

        while True:
            clear_console()
            imgList = [k for k in filenames if '.jpg' in k]
            img_filename = enquiries.choose('Please select an image to edit:', imgList)
            img_path = f'{folder_path}/{img_filename}'

            with open(img_path, 'rb') as img_file:
                img = Image(img_file)

                menu_selected = enquiries.choose('Please select function: ', menu_options)
                selectFunction(menu_selected, img)
    except KeyboardInterrupt:
        print("Bye! See you next time!")


if __name__ == "__main__":
    main()

        