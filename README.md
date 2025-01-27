# Contour Detection Script

This Python script is designed for detecting contours in an image, drawing bounding rectangles around detected contours, and visualizing the result using OpenCV.

## Features
- Reads and processes an input image.
- Converts the image to grayscale and applies Gaussian blur for noise reduction.
- Uses a thresholding technique to isolate bright regions in the image.
- Detects contours using OpenCV's `findContours` method.
- Draws contours and bounding rectangles on the original image for visualization.
- Displays the processed images using OpenCV's GUI.

## Requirements
To run this script, you need the following dependencies:
- Python 3.x
- OpenCV (`cv2`)
- NumPy (optional, but recommended for image processing tasks)

## Setup Instructions
1. Install Python if it's not already installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the required Python libraries using pip:
   ```bash
   pip install opencv-python
   ```
3. Place your input image in a directory named `imgs` in the same folder as this script. Rename the image to `Happy-Guy.jpg`, or modify the `image_path` in the script to match your image file's path and name.

## Usage
1. Run the script by executing the following command in your terminal or command prompt:
   ```bash
   python contours.py
   ```
2. The script will process the image and display the following:
   - Original Image with contours and bounding rectangles drawn.
   - Grayscale version of the image.
   - Thresholded binary image.

## Code Explanation
- **Image Reading and Preprocessing**:
  The script reads the image from the `imgs` folder, resizes it, converts it to grayscale, and applies Gaussian blur to smoothen the image and reduce noise.

- **Thresholding**:
  A binary threshold is applied to create a mask where the bright areas are set to white (255) and the rest to black (0).

- **Contour Detection**:
  Contours are identified in the binary image, and their areas are calculated. Contours with an area greater than 2000 pixels are highlighted in red and enclosed in a bounding rectangle.

- **Visualization**:
  The processed images are displayed in separate windows using OpenCV's `imshow` function. Press any key to close the windows.

## Customization
- Modify the thresholding parameters (`cv2.threshold`) to adjust which regions are detected as contours.
- Change the contour area filter (`if cv2.contourArea(cont) > 2000`) to detect smaller or larger contours.
- Update the `image_path` variable to work with different images.

## Notes
- The script is set to work with an image named `Happy-Guy.jpg` in the `imgs` directory by default. Ensure this file exists or update the script to use your image.
- The script uses `cv2.imshow` to display images, which requires a GUI environment. It may not work in a headless setup like some remote servers.



