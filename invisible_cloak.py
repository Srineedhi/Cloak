
import cv2
import numpy as np
import time

CAMERA_INDEX = 0
BACKGROUND_FRAMES = 40

# HSV range for purple clothing (OpenCV hue: 0–179)
LOWER_PURPLE = np.array([120, 40, 40], dtype=np.uint8)
UPPER_PURPLE = np.array([170, 255, 255], dtype=np.uint8)

WINDOW_NAME = "Purple Invisible Cloak | ESC to Exit"


def capture_background(cap):
    """Capture and average multiple empty-background frames."""
    print("Move away from the camera...")
    print("Capturing background in 3 seconds.")

    time.sleep(3)
    frames = []

    for _ in range(BACKGROUND_FRAMES):
        ret, frame = cap.read()

        if not ret:
            raise RuntimeError("Could not capture the background.")

        frame = cv2.flip(frame, 1)
        frames.append(frame.astype(np.float32))

    background = np.mean(frames, axis=0).astype(np.uint8)

    print("Background captured successfully.")
    return background


def create_cloak_mask(frame):
    """Detect purple regions and reduce mask noise."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, LOWER_PURPLE, UPPER_PURPLE)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_CLOSE, kernel
    )
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Smooth the mask for softer edges.
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    return mask


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    try:
        # Allow the webcam to initialize.
        time.sleep(1)

        background = capture_background(cap)

        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Warning: Unable to read camera frame.")
                break

            frame = cv2.flip(frame, 1)

            # Resize background if the camera resolution changes.
            if background.shape != frame.shape:
                background = cv2.resize(
                    background,
                    (frame.shape[1], frame.shape[0])
                )

            mask = create_cloak_mask(frame)

            # Convert mask into a smooth blending weight.
            alpha = mask.astype(np.float32) / 255.0
            alpha = alpha[:, :, np.newaxis]

            # Purple regions show the captured background.
            output = (
                frame.astype(np.float32) * (1.0 - alpha)
                + background.astype(np.float32) * alpha
            )

            output = np.clip(output, 0, 255).astype(np.uint8)

            cv2.imshow(WINDOW_NAME, output)

            key = cv2.waitKey(1) & 0xFF

            if key == 27 or key == ord("q"):
                break

    except RuntimeError as error:
        print(f"Camera error: {error}")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera released. Cloak application closed.")


if __name__ == "__main__":
    main()
