import flet as ft
import base64
import cv2

cap = cv2.VideoCapture(0)

class Rec(ft.UserControl):
    def __init__(self):
        super().__init__()

    def did_mount(self):
        self.update_timer()

    def update_timer(self):
        while True:
            _, frame = cap.read()
            # frame = cv2.resize(frame,(400,400))
            _, im_arr = cv2.imencode('.png', frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        self.img = ft.Image(
            border_radius=ft.border_radius.all(20)
        )
        return self.img
