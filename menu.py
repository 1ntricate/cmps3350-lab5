# Alberto Munoz
# CMPS 3350
# lab5 
# This script will display a menu for the user to choose wich action they want
# STILL IN PROGRESS!!

# import functions
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from crop import crop_image
from resize import resize_image


def display_menu():
    print("1. Import Image")
    print("2. Crop")
    print("3. Resize")
    print("4. Recolor")
    print("5. Quit")

def get_user_choice():
    try:
        choice = int(input("Please select one of the feautures: "))
        return choice
    except ValueError:
        print("Invalid input: Please enter a number that is listed.")
        return None

imported_image = None
# current_image

while True:
    display_menu()
    user_choice = get_user_choice()

    if user_choice is not None:
        if user_choice == 1:
            try:
                file_path = input("Enter the filepath to your image file: ")
                # Store a copy of OG image
                # current_image will store changes made
            except IOError:
                print("There was an error saving the inputted file, please try again.")
        if user_choice == 2:
            cropped_image = crop_image(file_path)
            plt.imshow(cropped_image)
            plt.axis('on')
            plt.show()
        if user_choice == 3:
            resized_image = resize_image(file_path)
            plt.imshow(resized_image)
            plt.axis('on')
            plt.show()
        # Recolor feature implemented here
        if user_choice == 5:
            print("Goodbye.")
            exit()



            
