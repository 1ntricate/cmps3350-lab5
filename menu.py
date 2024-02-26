# Alberto Munoz
# CMPS 3350
# lab5 
# This script will display a menu for the user to choose wich action they want
# STILL IN PROGRESS!!

# import functions
from PIL import Image
from crop import crop_image

def display_menu():
    print("1. Import Image")
    print("2. Crop")
    print("3. Resize")
    print("4. Quit")

def get_user_choice():
    try:
        choice = int(input("Please select one of the feautures: "))
        return choice
    except ValueError:
        print("Invalid input: Please enter a number that is listed.")
        return None

imported_image = None

while True:
    display_menu()
    user_choice = get_user_choice()

    if user_choice is not None:
        if user_choice == 1:
            try:
                file_path = input("Enter the filepath to your image file: ")
            except IOError:
                print("There was an error saving the inputted file, please try again.")
        if user_choice == 2:
            cropped_image = crop_image(file_path)
            cropped_image.show()



            
