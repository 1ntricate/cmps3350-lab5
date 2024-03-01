# Alberto Munoz

from PIL import Image

def resize_image(input_image):

    # Function allows user to resize image by inputing
    # width and height

    try:
        # Open the image file
        image = Image.open(input_image)
        
        # Ask user for new width and height
        width = int(input("Enter your desired width: "))
        height = int(input("Enter your desired height: "))
        
        # Resize image
        resized_image = image.resize((width, height))
        return resized_image
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

