import cv2
import mediapipe as mp

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.75, trackCon=0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """Detects hands in the input image and draws landmarks if enabled."""
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS,
                        self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2),  # Green connections
                        self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2)   # Green points
                    )
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """Returns a list of landmark positions for a specific hand."""
        lmList = []
        if self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):  # Ensure valid hand index
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 6, (255, 0, 0), cv2.FILLED)  # Blue dots
        return lmList
