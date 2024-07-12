import cv2
import numpy as np

def GaussianBlur_Kernel(size, sigma=1):
    # Create a Gaussian kernel based on the specified size and sigma
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(
            - ((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (size, size)
    )
    # Normalize the kernel
    return kernel / np.sum(kernel)

def Convolution(image, kernel):
    # Get the dimensions of the image and the kernel
    img_height, img_width, img_channels = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Pad the image to handle borders
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), mode='constant')

    # Initialize the output image
    output = np.zeros((img_height, img_width, img_channels))

    # Apply the convolution operation
    for y in range(img_height):
        for x in range(img_width):
            for c in range(img_channels):
                output[y, x, c] = np.sum(padded_image[y:y + kernel_height, x:x + kernel_width, c] * kernel)

    # Convert the output to an unsigned 8-bit integer type
    return output.astype(np.uint8)

# Read the image
img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

# Create a Gaussian kernel
kernel = GaussianBlur_Kernel(15, 5)

# Apply the custom convolution function with the Gaussian kernel
BlurImg = Convolution(img, kernel)

# Apply OpenCV's GaussianBlur function for comparison
BlurImgCV2 = cv2.GaussianBlur(img, (15, 15), 5)

# Display the original image
cv2.imshow('Original Image', img)

# Display the image blurred with the custom convolution function
cv2.imshow('Blurred Image', BlurImg)

# Display the image blurred with OpenCV's GaussianBlur function
cv2.imshow('Blurred Image With CV2', BlurImgCV2)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
