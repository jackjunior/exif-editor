from constants import UPDATE_MENU_OPTIONS
import enquiries, os, re
from datetime import datetime

def checkExifValue(attribute, image):
    return True if image.get(attribute) is not None else False

def printImageExif(image):    
    if checkExifValue("acceleration", image): print (f'Acceleration: {image.get("acceleration")}')
    if checkExifValue("model", image): print (f'Model: {image.get("model")}')
    if checkExifValue("artist", image): print (f'Artist: {image.get("artist")}')
    if checkExifValue("brightness_value", image): print (f'Brightness Value: {image.get("brightness_value")}')
    if checkExifValue("color_space", image): print (f'Color Space: {image.get("color_space")}')
    if checkExifValue("components_configuration", image): print (f'Components Configuration: {image.get("components_configuration")}')
    if checkExifValue("compression", image): print (f'Compression: {image.get("compression")}')
    if checkExifValue("datetime", image): print (f'Date Time: {image.get("datetime")}')
    if checkExifValue("datetime_digitized", image): print (f'Date Time Digitized: {image.get("datetime_digitized")}')
    if checkExifValue("datetime_original", image): print (f'Date Time Original: {image.get("datetime_original")}')
    if checkExifValue("device_setting_description", image): print (f'Device Setting Description: {image.get("device_setting_description")}')
    if checkExifValue("color_space", image): print (f'Color Space: {image.get("color_space")}')
    if checkExifValue("color_space", image): print (f'Color Space: {image.get("color_space")}')
    
    input("Press Enter to continue...")

def selectFunction(menu_selection, image):
    if menu_selection[0:1] == "1": printImageExif(image)
    if menu_selection[0:1] == "2": updateExifTag(image)
    if menu_selection[0:1] == "3": printImageExif(image)
    if menu_selection[0:1] == "4": raise KeyboardInterrupt
    if menu_selection[0:1] == "5": printImageExif(image)
    if menu_selection[0:1] == "6": printImageExif(image)

def updateExifTag(image):
    while True:
        clear_console()
        update_menu_selected = enquiries.choose('Please select update item: ', UPDATE_MENU_OPTIONS)
        if update_menu_selected[0:1] == "1": 
            # Original datetime that image was taken (photographed)
            print(f'DateTime (Original): {image.get("datetime_original")}')
            datetime_input = input("Enter the image new date - (yyyy/mm/dd): ")
            validate_datetime(datetime_input)
            input("Press Enter to continue...")
        if update_menu_selected[0:1] == "2": break;

def validate_datetime(input_string):
    # Define the expected format
    format = '%Y/%m/%d %H:%M:%S'
    
    # Define the regular expression pattern for allowed characters
    pattern = r'^[0-9/ :]+$'
    
    # Check if the input string contains only allowed characters
    if not re.match(pattern, input_string):
        print(f"Invalid characters in date/time string: {input_string}. Allowed characters: 0-9, /, :, space")
    
    try:
        # Try to create a datetime object using the format
        datetime_obj = datetime.strptime(input_string, format)
        # If parsing is successful, return the datetime object
        return datetime_obj
    except ValueError as e:
        # If parsing fails, return an error message
        print(f"Invalid date/time format: {input_string}. Expected format: yyyy/mm/dd hh:mm:ss")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# def saveEditedImage(image):
#     with open(f'{folder_path}/{img_filename}', 'wb') as new_image_file:
#                 new_image_file.write(img.get_file())