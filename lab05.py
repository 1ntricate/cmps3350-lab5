# Alberto Munoz
# Nathan Nguyen

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def resize_image(input_image):
    try:
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
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image
    except Exception as e:
        print(f"Error cropping image: {e}")
        return None

def recolor_image(input_image, r_shift, g_shift, b_shift, a_shift):
    try:
        image = Image.open(input_image)
        pixels = image.load()
        width, height = image.size
        for y in range(height):
            for x in range(width):
                try:
                    r, g, b, a = pixels[x, y]
                except ValueError:
                    # If image doesn't have alpha channel, assume fully opaque
                    r, g, b = pixels[x, y]
                    a = 255
                r = max(0, min(255, r + r_shift))
                g = max(0, min(255, g + g_shift))
                b = max(0, min(255, b + b_shift))
                a = max(0, min(255, a + a_shift))
                pixels[x, y] = (r, g, b, a)
        return image
    except Exception as e:
        print(f"Error recoloring image: {e}")
        return None

def main():
    while True:
        # Display the original image
        img = mpimg.imread('mikus.png')
        plt.imshow(img)
        plt.axis('on')  # Optional: Turn off axes
        plt.show()

        # Prompt for action
        action = input("Enter 'r' to resize, 'c' to crop, 're' to recolor, or 'q' to quit: ")

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
        elif action == 're':
            # Recolor the image
            r_shift = int(input("Enter red shift value (integer): "))
            g_shift = int(input("Enter green shift value (integer): "))
            b_shift = int(input("Enter blue shift value (integer): "))
            a_shift = int(input("Enter alpha shift value (integer): "))
            recolored_img = recolor_image('mikus.png', r_shift, g_shift, b_shift, a_shift)
            if recolored_img:
                plt.imshow(recolored_img)
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
