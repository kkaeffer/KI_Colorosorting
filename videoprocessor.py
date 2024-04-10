import flet as ft
import base64
import cv2
from rec import Rec

cap = cv2.VideoCapture(0)

# VideoProcessor-Klasse für die Videoaufnahme
class VideoProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame