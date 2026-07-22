# OpenCV Object Detection

Real-time color-based object detection and tracking with OpenCV webcam input.

---

## English

### About
Click a color on the live camera feed. The app builds an HSV range around that color, detects matching objects, assigns track IDs, and draws them on the frame.

**Author:** Veronika Yuzik  
**Context:** Prepared during training for the **IOAI Ukraine** olympiad (International Olympiad in Artificial Intelligence).

### Features
- Webcam capture
- Color pick by mouse click
- HSV mask + object detection
- Multi-object tracking with IDs
- Press `q` to quit

### Project structure

    main.py              # entry point
    capture/             # camera / stream
    detection/           # color mask
    tracking/            # object tracking
    display/             # drawing overlays
    config.py            # settings

### Install

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install opencv-python numpy

### Run

    python main.py

### Controls
| Action | How |
|--------|-----|
| Pick color | Left mouse click on the frame |
| Quit | `q` |

---

## Українською

### Про проєкт
Клікніть по кольору на відео з камери. Програма будує HSV-діапазон навколо цього кольору, знаходить відповідні об'єкти, дає їм track ID і малює на кадрі.

**Автор:** Veronika Yuzik  
**Контекст:** Підготовка до олімпіади **IOAI України** (Міжнародна олімпіада зі штучного інтелекту).

### Можливості
- Захоплення з веб-камери
- Вибір кольору кліком миші
- HSV-маска + детекція об'єктів
- Трекінг кількох об'єктів з ID
- Вихід клавішею `q`

### Структура проєкту

    main.py              # точка входу
    capture/             # камера / стрім
    detection/           # колірна маска
    tracking/            # трекінг об'єктів
    display/             # малювання
    config.py            # налаштування

### Встановлення

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install opencv-python numpy

### Запуск

    python main.py

### Керування
| Дія | Як |
|-----|----|
| Вибрати колір | Лівий клік миші по кадру |
| Вийти | `q` |
