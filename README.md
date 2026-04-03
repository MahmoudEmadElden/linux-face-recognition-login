# 🐧 Linux Face Recognition Login 🐧💻

Unlock your laptop using your face with **Howdy**!

Are you a Linux user tired of typing your password every time you open your laptop or run `sudo`? This project brings **Windows Hello-style facial authentication** to your Linux machine using OpenCV and dlib.

---

## 🚀 Features
- **Facial Authentication**: Log in and unlock your screen using your camera.
- **Sudo Integration**: Authenticate root commands in the terminal with your face.
- **PAM-based**: Securely integrated into the system's Pluggable Authentication Modules.
- **Fast & Accurate**: Uses dlib's state-of-the-art face recognition models.

---

## 🛠️ Prerequisites & Dependencies
To run this, you need a functional camera (standard RGB or IR) and the following dependencies:
- **Howdy**: The facial recognition engine.
- **libpam-python**: To interface with the PAM system.
- **python3-opencv**: For video stream handling.
- **python3-dlib**: For facial landmark detection and recognition.
- **python-setuptools**, **ninja-build**, **meson** (for building models).

---

## ⚙️ Installation (Quick Start)
1. **Install Dependencies**:
   ```bash
   sudo apt-get install python3-opencv v4l-utils libpam-python
   ```
2. **Download & Install Howdy**:
   Follow the instructions on the [official Howdy GitHub repository](https://github.com/boltgolt/howdy).
3. **Configure Your Camera**:
   Find your camera path (usually `/dev/video0`) and set it in `/etc/howdy/config.ini`:
   ```ini
   device_path = /dev/video0
   ```
4. **Enroll Your Face**:
   ```bash
   sudo howdy add
   ```

---

## 🔒 Security Notice
Face recognition is designed for **convenience**, not high security. While IR cameras offer better protection against photos, it is not as secure as a strong password. Use it at your own discretion.

---

## 🤝 Credits & Acknowledgements
This project is built upon the amazing work of [boltgolt/howdy](https://github.com/boltgolt/howdy) and the **dlib** face recognition models.

#Linux #OpenCV #FaceRecognition #Howdy #KaliLinux #CyberSecurity #Automation #Productivity
