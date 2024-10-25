"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/
"""
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from convolution import convolution

# Sobel edge detection function
def sobel_edge_detection(image, filter, verbose=False):
    new_image_x = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    new_image_y = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()

    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude

if __name__ == '__main__':
    # Sobel filter mask/kernel
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    # Argument parser to get image arguments from the shell
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=False, help="Path to the image")
    args = vars(ap.parse_args())

    # Set the image path from the arguments or use the default path
    image_path = args.get("image")

    # Use the default image path if none is provided
    if image_path is None:
        image_path = r"D:\ESCUELA\Laboratorio\Vision-ST\image.jpg"

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    # Apply Sobel edge detection
    sobel_edge_detection(image, filter, verbose=True)
