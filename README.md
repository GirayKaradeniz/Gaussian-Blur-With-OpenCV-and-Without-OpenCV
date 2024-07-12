# Gaussian-Blur-With-OpenCV-and-Without-OpenCV

This project demonstrates the creation and application of a Gaussian blur to an image using both a custom convolution function and OpenCV's built-in Gaussian blur function. The project reads an image, generates a Gaussian kernel, applies the blur, and displays the original and blurred images for comparison.

## Table of Contents

+ Introduction
+ Requirements
+ Usage
+ Code Explanation

## Introduction

Gaussian blur is a widely used effect in graphics software, typically to reduce image noise and detail. This project showcases how to manually implement Gaussian blur using a custom convolution function and compares the result with OpenCV's built-in Gaussian blur function.

## Requirements

+ Python 3.x
+ OpenCV
+ NumPy

## Usage

Ensure you have an image named Lenna.png in the project directory. You can replace this with any image of your choice.

Run the script:

```bash
python GaussianBlur.py
The script will display three windows:
```
The script will display three windows:

+ Original Image
+ Blurred Image (Custom Convolution)
+ Blurred Image (OpenCV)

## Code Explanation

+ GaussianBlur_Kernel(size, sigma): Generates a Gaussian kernel of specified size and standard deviation.
+ Convolution(image, kernel): Applies the convolution operation between the image and the kernel.
+ The script reads an image, generates a Gaussian kernel, applies the custom convolution and OpenCV's Gaussian blur, and displays the results for comparison.
