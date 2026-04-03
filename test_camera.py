import cv2

def test_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    ret, frame = cap.read()
    if ret:
        print("Camera is working. Captured a frame.")
        cv2.imwrite("/home/noone/cameraa/test_frame.jpg", frame)
        print("Saved test frame to /home/noone/cameraa/test_frame.jpg")
    else:
        print("Error: Could not read frame.")
    
    cap.release()

if __name__ == "__main__":
    test_camera()
