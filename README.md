# Cloak — Purple Invisible Cloak

### Real-Time Background Replacement Using OpenCV

## Overview

Cloak is a computer vision project that creates an invisible-cloak visual effect using a webcam. It detects purple-colored regions in the video stream and replaces them with a previously captured background, making the selected region appear invisible.

The project uses Python, OpenCV, and NumPy for real-time video capture, HSV-based color segmentation, image masking, and background compositing.

## Features

- **Real-time webcam processing:** Captures and processes live video frames.
- **Background capture:** Records the scene before the user enters the camera view.
- **Purple color detection:** Uses HSV color thresholds to identify purple clothing.
- **Image masking:** Separates the selected color region from the rest of the frame.
- **Background replacement:** Replaces detected regions with the captured background.
- **Mask refinement:** Applies morphological operations and smoothing to reduce noise and soften edges.
- **Safe exit:** Supports keyboard controls to close the application and release the camera.

## Technology Stack

- **Language:** Python
- **Computer Vision:** OpenCV
- **Numerical Processing:** NumPy
- **Input Device:** Webcam

## How It Works

1. **Initialize the camera:** OpenCV accesses the webcam and starts reading frames.
2. **Capture the background:** Multiple frames are collected while the scene is empty and combined to create a background image.
3. **Convert to HSV:** Each live frame is converted from BGR to HSV color space.
4. **Detect purple:** A color threshold creates a mask for purple-colored regions.
5. **Refine the mask:** Morphological operations remove small noise and improve the selected region.
6. **Replace the region:** Pixels identified as purple are replaced with pixels from the captured background.
7. **Display the output:** The processed frame is shown continuously until the user exits.

## Project Structure

```text
Cloak/
├── invisible_cloak.py
└── raw.hs.html
```

- `invisible_cloak.py` — Python implementation of the invisible-cloak effect.
- `raw.hs.html` — HTML interface for the HYDRONEXUS H₂S Safety Monitor.

These files represent separate components unless they are explicitly integrated.

## Prerequisites

- Python 3.9 or later recommended
- A working webcam
- Windows, macOS, or Linux
- `pip` package manager

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Srineedhi/Cloak.git
cd Cloak
```

### 2. Install dependencies

```bash
python -m pip install opencv-python numpy
```

### 3. Run the application

```bash
python invisible_cloak.py
```

When prompted, move out of the camera's field of view while the background is captured. Then wear a purple garment and enter the frame.

Press **Esc** or **Q** to exit.

## Configuration

The purple detection range can be adjusted in `invisible_cloak.py`:

```python
LOWER_PURPLE = np.array([120, 40, 40])
UPPER_PURPLE = np.array([170, 255, 255])
```

The ideal HSV range depends on the garment's shade and the lighting conditions.

The webcam index can also be changed if the default camera is unavailable.

## Limitations

- Performance depends on lighting and the shade of purple.
- The camera and background should remain stationary after background capture.
- Purple objects in the background may also be detected.
- Occlusion, shadows, and rapid movement can affect the visual result.
- The effect is image compositing and does not provide actual invisibility.

## Future Improvements

- Interactive color selection.
- Adjustable HSV thresholds.
- More robust segmentation and edge refinement.
- Support for selecting different webcam devices.
- A graphical interface with live camera status and capture controls.
- Automated testing for image-processing functions.

## Learning Outcomes

This project demonstrates practical concepts in computer vision, HSV color spaces, image segmentation, morphological filtering, real-time video processing, and background compositing.

## Author

**Srineedhi R**

## License

This project is available under the MIT License. See the `LICENSE` file for the full terms.

If a `LICENSE` file has not yet been added, create one before describing the repository as formally licensed under MIT.
