# OpenCV Learning README

## Goal

Learn Computer Vision fundamentals using OpenCV for AI/ML projects and future open-source contributions.

## Session 1 Progress

### Concepts Learned

* Images are NumPy arrays.
* Color image shape: `(Height, Width, 3)`.
* Grayscale image shape: `(Height, Width)`.
* Pixels and image indexing.
* BGR color representation.
* Color channels:

  * `img[:,:,0]` → Blue
  * `img[:,:,1]` → Green
  * `img[:,:,2]` → Red
* Cropping using slicing.
* Resizing images.
* OpenCV coordinates `(x, y)` vs NumPy indexing `[row, col]`.
* Drawing rectangles.
* Understanding coordinates, margins, and thickness.
* Converting images to grayscale.
* Gaussian Blur:

  * Kernel size (e.g. `(5,5)`)
  * Noise reduction and smoothing
  * Basic understanding of `sigmaX`
* Edge Detection (Canny):

  * Lower and upper thresholds
  * Effect of threshold values
  * Comparison of color vs grayscale edge detection
* Thresholding:

  * Binary thresholding
  * Threshold value and max value
  * Understanding `ret`
  * `THRESH_BINARY` vs `THRESH_BINARY_INV`
* Contours:

  * Detecting contours using `cv2.findContours()`
  * Understanding `contours` as a collection of boundaries
  * Each contour is a NumPy array of boundary points
  * Basic contour structure and indexing

## Current Position

* Contours (understanding contour properties and applications).
