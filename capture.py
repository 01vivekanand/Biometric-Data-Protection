import cv2

def capture_image(filename="scan.jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    if ret:
        cv2.imwrite(filename, frame)
        print("Image captured:", filename)
    else:
        print("Failed to capture image")

    cam.release()

if __name__ == "__main__":
    capture_image()