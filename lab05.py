# Alberto Munoz
# Nathan Nguyen

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def resize_image(input_image):
    try:
        #Open The image file/ask for image resized
        image = Image.open(input_image)
        width = int(input("Enter your desired width: "))
        height = int(input("Enter your desired height: "))
        resized_image = image.resize((width, height))
        return resized_image
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

def crop_image(input_image):
    try:
        image = Image.open(input_image)
        left = int(input("Enter left coordinate: "))
        top = int(input("Enter top coordinate : "))
        right = int(input("Enter right coordinate : "))
        bottom = int(input("Enter bottom coordinate : "))

        # Check if cropping coordinates are valid
        if right <= left or bottom <= top:
            print("Invalid cropping coordinates.")
            return None

        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image
    except Exception as e:
        print(f"Error cropping image: {e}")
        return None

def main():
    while True:
        # Display the original image
        img = mpimg.imread('mikus.png')
        plt.imshow(img)
        plt.axis('on')  # Optional: Turn off axes
        plt.show()

        # Prompt for action
        action = input("Enter 'r' to resize, 'c' to crop, or 'q' to quit: ")

        if action == 'r':
            # Resize the image
            resized_img = resize_image('mikus.png')
            if resized_img:
                plt.imshow(resized_img)
                plt.axis('on')  # Optional: Turn off axes
                plt.show()
        elif action == 'c':
            # Crop the image
            cropped_img = crop_image('mikus.png')
            if cropped_img:
                plt.imshow(cropped_img)
                plt.axis('on')  # Optional: Turn off axes
                plt.show()
        elif action == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

    print("hello world")

if __name__ == "__main__":
    main()
