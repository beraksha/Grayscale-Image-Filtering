from PIL import Image
import numpy as np

def load_image(filepath):
    image = Image.open(filepath)
    return image.convert('L')

def bw_filter(image, k):
    image_array = np.array(image)
    im = np.zeros(image_array.shape, dtype=np.uint8)
    m = n = k // 2

    for x in range(image.width):
        for y in range(image.height):
            c = 0
            count = 0
            for i in range(-m, m + 1):
                for j in range(-m, m + 1):
                    if 0 <= x + i < image.width and 0 <= y + j < image.height:
                        c += image_array[y + j, x + i]
                        count += 1
            im[y, x] = c // count
    
    return Image.fromarray(im)

def show_image(image, title="Image"):
    image.show(title=title)

def main(filepath, mask_size):
    # Load the image
    original_image = load_image(filepath)
    
    # Display the original image
    show_image(original_image, title="Original Image")
    
    # Apply the black & white filter
    filtered_image = bw_filter(original_image, mask_size)
    
    # Display the filtered image
    show_image(filtered_image, title="Filtered Image")

if __name__ == "__main__":
    # Example usage
    filepath = r"C:\Users\Raksha Eshwar\Pictures\Photos\IMG_0331.jpg"
    mask_size = 3
    main(filepath, mask_size)

