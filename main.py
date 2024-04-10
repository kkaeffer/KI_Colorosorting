# main.py
# test

import flet as ft
import base64
import cv2
from rec import Rec
from videoprocessor import VideoProcessor

processor = VideoProcessor()

def height_changed(e):
    print(e.control.value)

section = ft.Container(
    margin=ft.margin.only(bottom=40),
    content=ft.Row([
        ft.Card(
            elevation=30,
            content=ft.Container(
                bgcolor=ft.colors.WHITE24,
                padding=10,
                border_radius = ft.border_radius.all(20),
                content=ft.Column([
                    Rec(),
                    ft.Text("Colorsorting",
                         size=20, weight="bold",
                         color=ft.colors.WHITE),
                ]
                ),
            )
        ),
        ft.Card(
            elevation=30,
            content=ft.Container(
                bgcolor=ft.colors.WHITE24,
                padding=10,
                border_radius=ft.border_radius.all(20),
                content=ft.Column([
                    ft.CupertinoButton(text="Aufnahme", bgcolor="green"),
                    ft.CupertinoButton(text="ClickClick", bgcolor="green"),
                    ft.CupertinoButton(text="ClickClick", bgcolor="green")
                ]
                ),

            )
        )
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
)

def main(page: ft.Page):
    page.padding = 50
    page.window_left = page.window_left+100
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        section,
    )

if __name__ == '__main__':
    processor = VideoProcessor()
    cap = processor.cap
    frame = processor.get_frame()
    ft.app(target=main)
    cap.release()
    cv2.destroyAllWindows()

"""
def main(page: ft.Page):
    
    columncontainer = ft.Column(controls=[ft.CupertinoButton(text="ClickClick", bgcolor="green")])
    container = ft.Container(content=columncontainer,alignment=ft.alignment.center)
    
    page.add(ft.SafeArea(ft.Text("Schweinedöner!!!")))
    page.add(container)
    
    
def ichwurdegeklickt(e, page):
    for i in range(10):
        page.update()
        time.sleep(0.3)
            
    print("Hallo Welt!")

ft.app(main)

"""