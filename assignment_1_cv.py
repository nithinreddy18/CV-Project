# -*- coding: utf-8 -*-
"""Assignment 1 CV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JwJrwBDNx_ywIbEH6WwbjNebgRHRCPJY
"""

from PIL import Image
from numpy import array
import cv2 as cv
im_1 = cv.imread("/content/fracture.png")
ar = array(im_1)
ar

from PIL import Image
import matplotlib.pyplot as plt
# Open an image
image = Image.open("/content/image_3.jpg")
# Convert the image to grayscale (optional)
image = image.convert("L")
# Calculate the histogram
histogram = image.histogram()
# Plot the histogram
plt.hist(histogram, bins=256, range=(0, 256), density=True,
color='gray', alpha=0.7)
plt.title("Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

from PIL import Image
import numpy as np
from google.colab.patches import cv2_imshow
def histogram_equalization(image):
# Convert the image to grayscale
# Convert the image to a NumPy array
    img_array = np.array(image)
# Calculate the histogram
    hist, bins = np.histogram(img_array, bins=256, range=(0, 256))
# Calculate the cumulative distribution function (CDF)
    cdf = hist.cumsum()
# Apply histogram equalization to the image
    cdf_min = cdf.min()
    img_eq = (cdf[img_array] - cdf_min) * 255 / (cdf[-1] - cdf_min)
# Convert the equalized NumPy array back to an image
    equalized_image = Image.fromarray(np.uint8(img_eq))
    return equalized_image
# Open an image
image = Image.open("/content/fracture.png")
ima=cv.imread("/content/fracture.png")
cv2_imshow(ima)
# Perform histogram equalization
equalized_image = histogram_equalization(image)
# Display the original and equalized imag
equalized_image

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

# Open an image
image = Image.open("/content/th.jpeg")

# Apply Gaussian smoothing to the image
smoothed_image = image.filter(ImageFilter.GaussianBlur(radius=1))

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image on the first subplot
ax1.set_title("Original Image")
ax1.imshow(image)
ax1.axis('off')

# Display the smoothed image on the second subplot
ax2.set_title("Smoothed Image")
ax2.imshow(smoothed_image)
ax2.axis('off')

# Show the figure with both images
plt.show()

import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import cv2
# Load an image
image = cv2.imread("/content/image_3.jpg", cv2.IMREAD_GRAYSCALE)
# Compute the first-order derivative along the x and y axes
dx = np.array([[-1, 0, 1]])
dy = dx.T
dx_derivative = convolve(image, dx)
dy_derivative = convolve(image, dy)
# Display the original image and its first-order derivatives
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(132)
plt.imshow(dx_derivative, cmap="gray")
plt.title("First-Order Derivative (X-axis)")
plt.subplot(133)
plt.imshow(dy_derivative, cmap="gray")
plt.title("First-Order Derivative (Y-axis)")
plt.tight_layout()
plt.show()

import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

# Load an image (make sure to provide the correct file path)
image = plt.imread("/content/fracture.png")

# Convert the image to grayscale if it's in color
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Define a Laplacian kernel for second-order derivative
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Calculate the second-order derivative using convolution
second_order_derivative = convolve(image, laplacian_kernel)

# Display the original image and its second-order derivative
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(122)
plt.imshow(second_order_derivative, cmap="gray")
plt.title("Second-Order Derivative (Laplacian)")
plt.tight_layout()
plt.show()

import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Load an image (provide the correct file path)
image = plt.imread("/content/fracture.png")

# Convert the image to grayscale if it's in color
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Define Sobel operators for gradient calculation
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply the Sobel operators to calculate gradients
gradient_x = convolve2d(image, sobel_x, mode='same', boundary='wrap')
gradient_y = convolve2d(image, sobel_y, mode='same', boundary='wrap')

# Calculate the magnitude of the gradient
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Display the original image, Sobel gradients, and gradient magnitude
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(132)
plt.imshow(gradient_x, cmap="gray")
plt.title("Sobel X-Gradient")
plt.subplot(133)
plt.imshow(gradient_y, cmap="gray")
plt.title("Sobel Y-Gradient")
plt.tight_layout()
plt.show()

# Display the gradient magnitude
plt.figure(figsize=(6, 6))
plt.imshow(gradient_magnitude, cmap="gray")
plt.title("Gradient Magnitude")
plt.show()

import numpy as np
from scipy.ndimage import label, generate_binary_structure
from skimage import measure
import matplotlib.pyplot as plt

# Load an image (provide the correct file path)
image = plt.imread("/content/th (1).jpeg")

# Convert the image to grayscale if it's in color
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Threshold the image to create a binary mask
binary_image = image > 128  # You can adjust the threshold as needed

# Label connected components in the binary image
structure = generate_binary_structure(2, 2)
labeled_image, num_labels = label(binary_image, structure)

# Create an RGB image for drawing borders
border_image = np.stack([image] * 3, axis=-1)  # Create a 3-channel image
border_color = [255, 0, 0]  # Red color

# Find and draw object borders
for label in range(1, num_labels + 1):
    labeled_mask = labeled_image == label
    contours = measure.find_contours(labeled_mask, 0.5)
    for contour in contours:
        for row, col in contour:
            border_image[int(row), int(col)] = border_color

# Display the original image and object borders
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(122)
plt.imshow(border_image)
plt.title("Object Borders")
plt.tight_layout()
plt.show()

import numpy as np
from scipy.ndimage import label, generate_binary_structure
from skimage import measure
import matplotlib.pyplot as plt

# Load an image (provide the correct file path)
image = plt.imread("/content/image_3.jpg")

# Convert the image to grayscale if it's in color
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Threshold the image to create a binary mask
binary_image = image > 128  # You can adjust the threshold as needed

# Label connected components in the binary image
structure = generate_binary_structure(2, 2)
labeled_image, num_labels = label(binary_image, structure)

# Create an RGB image for drawing borders
border_image = np.stack([image] * 3, axis=-1)  # Create a 3-channel image
border_color = [255, 0, 0]  # Red color

# Find and draw object borders
for label in range(1, num_labels + 1):
    labeled_mask = labeled_image == label
    contours = measure.find_contours(labeled_mask, 0.5)
    for contour in contours:
        for row, col in contour:
            border_image[int(row), int(col)] = border_color

# Display the original image and object borders
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.subplot(122)
plt.imshow(border_image)
plt.title("Object Borders")
plt.tight_layout()
plt.show()