import cv2
import numpy as np
import os

# import time

# WebCam Auflösung
width = 640  # Mögliche Kameraauflösungen (bei mir): 640x380, 640x380, 640x640, 1280x720
height = 480
# WebCam Rahmen, Region of Interest
rw = 224
rh = 224
cx = width // 2 - rw // 2  # Im Moment zentrierte Bildaufnahme
cy = height // 2 - rh // 2
p1 = (cx - 2, cy - 2)
p2 = (cx + rw + 2, cy + rh + 2)
size = (rw, rh)

# Weitere Einstellungen
framegap = 0.5  # für automatisierte Bildaufnahme, delay muss in der Schleife einkommentiert werden
MEINEFARBE = (255, 255, 255)
THICKNESS1 = 2

# Unterschiedlichen Klassen
classes = ["Rot", "Grün", "Blau", "Gelb", "Braun"]  # Hier belieibig viele Klassen angeben
class_iter = iter(classes)

# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# WebCam aktivieren
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('image')
path = './'
img_path = path
i = 0
while True:
    # time.sleep(framegap)

    # Tasten abhören
    k = cv2.waitKey(30)

    # Bei "c" -> Tasten funktionieren
    # Bei "n" -> erstelle einen neuen Ornder für eine neue Klasse; Bilder mit "s" aufzeichnen in diesen Ordner
    if k == ord('c'):
        print("c - gedrückt")
    elif k == ord('n'):  # erstelle einen neuen Ordner für die Bilder einer neuen Klassen
        try:
            cur_class = next(class_iter)
            print(f"Label: {cur_class}")
            if not os.path.exists(f'./{cur_class}'):
                os.system(f'mkdir {cur_class}')
            img_path = path + cur_class
            i = 0  # Reset Bild zähler
        except:
            print("Durch")
            break

    # Lies ein Bild
    ret, frame = cap.read()
    l, w, _ = frame.shape

    cv2.rectangle(frame, p1, p2, MEINEFARBE, THICKNESS1)
    img_part = frame[cy:cy + rh, cx:cx + rw, :]

    # Taste "s" -> Bildaufnahme
    if k == ord('s'):
        cv2.imwrite(img_path + f'/{str(i).zfill(4)}.png', img_part)
        i += 1
        print(
            f"{str(i).zfill(4)} Bild, Klasse: {cur_class} Aufloesung: {l}x{w}, x-Richtung: {cx}...{cx + rw}, y-Richtung: {cy}...{cy + rh} {img_path + f'/{str(i).zfill(4)}.png'}")

    # Bild anzeigen, Leertaste beendet
    cv2.imshow("image", frame)
    if cv2.waitKey(1) % 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()