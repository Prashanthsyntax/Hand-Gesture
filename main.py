import cv2
import mediapipe as mp
import time
import os
import subprocess
import HandTrackingModule as htm


app_map = {
    1: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",  # Open Chrome
    2: "C:\\Windows\\explorer.exe",  # Open File Explorer
    3: "C:\\Users\\prash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",  # Open VsCode
    4: "C:\\Windows\\system32\\calc.exe",  # Open Calculator
    5: "C:\\Windows\\notepad.exe",  # Open Notepad
}

# Camera setup
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize hand detector
detector = htm.handDetector(detectionCon=0.85)  # Increased confidence for better accuracy
tipIds = [4, 8, 12, 16, 20]  # IDs of fingertips (Thumb, Index, Middle, Ring, Pinky)

pTime = 0
last_open_time = 0  # Store the last time an app was opened
cooldown = 10  # Cooldown time in seconds
gesture_buffer = []  # Store recent finger counts
buffer_size = 5  # Number of frames to confirm a gesture
last_confirmed_fingers = -1  # Store the last confirmed gesture

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb (check x-coordinates for left/right hand)
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  
            fingers.append(1)  
        else:
            fingers.append(0)

        # Other 4 fingers (Index to Pinky)
        for i in range(1, 5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:  
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        current_time = time.time()

        # Buffering: Store last few detections to avoid fluctuations
        gesture_buffer.append(totalFingers)
        if len(gesture_buffer) > buffer_size:
            gesture_buffer.pop(0)

        # Only consider the gesture if all buffer frames match
        if gesture_buffer.count(gesture_buffer[0]) == buffer_size:
            confirmed_fingers = gesture_buffer[0]

            # Ensure it only opens if it's a new confirmed gesture
            if confirmed_fingers in app_map and confirmed_fingers != last_confirmed_fingers:
                if current_time - last_open_time > cooldown:
                    print(f"Opening: {app_map[confirmed_fingers]}")
                    subprocess.Popen(app_map[confirmed_fingers], shell=True)
                    last_open_time = current_time  # Update last open time
                    last_confirmed_fingers = confirmed_fingers  # Update last confirmed gesture

    # FPS Calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture App Launcher", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
