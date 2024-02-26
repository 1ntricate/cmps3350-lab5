from PIL import Image

def crop_image(input_image):
    
    try:
        # Open the image file
        image = Image.open(input_image)

        left = int(input("Enter left coordinate: "))
        top = int(input("Enter top coordinate : "))
        right = int(input("Enter right coordinate : "))
        bottom = int(input("Enter bottom coordinate : "))

        # Crop the image using inputted coordinates then return it
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image
    except Exception as e:
        print(f"Error cropping image: {e}" )
        return None


    



