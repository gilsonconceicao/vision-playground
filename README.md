# Camera CLI Project

A simple and curious project built in Python that allows the user to:

* Choose whether to open the computer camera
* Capture video in real-time
* Convert frames to grayscale
* Display the camera stream

This project was created as a learning exercise to explore **computer vision basics** using library OpenCV.

---

## Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy
* PyInputPlus

---

## What I Learned

Through this project, I was able to understand and practice:

* How to access the webcam using OpenCV
* Real-time frame capture and processing
* Converting images to grayscale
* Handling user input via CLI
* Basic control flow and state handling
* Proper resource cleanup (releasing camera and closing windows)

---

## ▶️ How It Works

1. The user is prompted:

   ```
   DESEJA ABRIR A CÂMERA [SIM | NAO]:
   ```

2. If the user selects `SIM`:

   * The camera is initialized
   * Frames are captured continuously
   * Each frame is converted to grayscale
   * The video is displayed in real time

3. The user can press:

   * `q` → to exit the camera

4. If the user selects `NAO`:

   * The program ends with a message

---

## 🖥️ Running the Project

### 1. Install dependencies

```bash
pip install opencv-python numpy pyinputplus
```

### 2. Run the script

```bash
python main.py
```
---

## Notes

* Make sure your camera is not being used by another application
* Press `q` to properly close the camera window
* The project uses the default camera (`index 0`)

---

## Future Improvements

Some ideas to evolve this project:

* Face detection
* Emotion recognition
* Motion detection
* Save images or recordings
