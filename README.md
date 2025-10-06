# Grayscale Image Filtering

This Python script applies a grayscale (black & white) mean filter to an image using PIL and NumPy. It reduces noise by averaging pixel intensities in a user-defined kernel neighborhood. Useful for image enhancement in fields like computer vision, medical imaging, and digital photography. 

Initially created for exploring Computer Graphics and it's concepts; and hence the script employs CG techniques like image representation as arrays, convolution-based filtering, and boundary-aware processing to smooth a grayscale image, demonstrating basic image processing concepts used in computer graphics. 

## Features
- Loads a color image and converts to grayscale.
- Applies mean filtering to smooth the image.
- Displays original and filtered images for comparison.

## Requirements
- Python 3.x
- Libraries:
  - `pillow` (install via `pip install pillow`)
  - `numpy` (install via `pip install numpy`)

## How to Run
1. Clone the repo: `git clone https://github.com/yourusername/grayscale-image-filtering.git`
2. Update the `filepath` in `grayscale_filter.py` to your image path.
3. Run: `python grayscale_filter.py`
- Kernel size (`mask_size`) defaults to 3; adjust for stronger/weaker smoothing.

### Notes
- The kernel size (mask_size) should be an odd number (e.g., 3, 5, 7) for symmetry.
- Ensure the image path is correct, or the script will raise a FileNotFoundError.
