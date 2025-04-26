# AirWave-X

AirWave-X is an AI-powered system that enables touch-free interaction by recognizing hand gestures via a webcam and seamlessly launching applications based on the gesture detected.

## 🚀 Features
- 🎯 Real-time hand gesture recognition using a webcam
- 🖐️ Detects finger counts (e.g., 1 finger → Launch LinkedIn, 2 fingers → Open Instagram, etc.)
- 📂 Launches installed applications automatically based on gestures
- 🔥 Smooth and fast touchless control
- 🧠 Built with Computer Vision (OpenCV) and Machine Learning
- 🖥️ Simple, lightweight, and highly responsive

## 🛠️ Tech Stack
- Python
- OpenCV
- Mediapipe (for hand landmark detection)
- pyautogui / os (for app launching)
- Other supporting libraries: numpy, etc.

## 📸 How It Works
1. The webcam captures live video feed.
2. AirWave-X analyzes hand landmarks and counts the number of fingers shown.
3. Depending on the detected gesture, it launches the mapped application.
4. Completely touch-free interaction!

## 🧩 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Prashanthsyntax/Hand-Gesture.git
   cd airwave-x
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## 📋 Gesture Mappings (example)
| Finger Count | Action              |
|--------------|---------------------|
| 1 Finger     | Open Chrome         |
| 2 Fingers    | Open File Explorer  |
| 3 Fingers    | Open VsCode         |
| 4 Fingers    | Open Calculator     |
| 5 Fingers    | Open Notepad        |

*(You can customize these mappings easily inside the code.)*

## 📂 Folder Structure
```
airwave-x/
│
├── main.py         # Main application file
├── HandTrackingModule.py     # Python dependencies
├── README.md            # Project documentation
└── Fingers              # (Optional) Icons, images, or other media
```

## 💡 Future Improvements
- Add voice feedback when an app is launched
- Train a custom hand gesture classifier for more complex actions
- Build a GUI dashboard to set custom app mappings

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and open a pull request.

## 📄 License
This project is licensed under the [MIT License](LICENSE).

## 🙌 Acknowledgements
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- Python Community 🚀
