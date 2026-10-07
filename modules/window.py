from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from .app import app

window = QWidget()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

size = app.primaryScreen().size()

window.setGeometry(
    (size.width() // 2) - (WIDTH_WINDOW // 2), 
    (size.height() // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

main_layout = QHBoxLayout(window)

bg = QFrame()
bg.setStyleSheet("background-color: black")
main_layout.addWidget(bg)

layout = QVBoxLayout(bg)
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(10)

title = QLabel("SPACE CONTROL")
title.setStyleSheet("color: white; font-size: 28px;")
layout.addWidget(title)

# статус
row1 = QHBoxLayout()
status = QFrame()
status.setFixedSize(500, 300)
status.setStyleSheet("background-color: gray")
status_label = QLabel("SYSTEM ONLINE", parent=status)
status_label.setStyleSheet("color: white; font-size: 22px;")
row1.addWidget(status)
row1.addWidget(QFrame())
layout.addLayout(row1)

# квадраты
grid = QGridLayout()

red = QFrame()
red.setFixedSize(100, 100)
red.setStyleSheet("background-color: red")

blue = QFrame()
blue.setFixedSize(100, 100)
blue.setStyleSheet("background-color: blue")

green = QFrame()
green.setFixedSize(100, 100)
green.setStyleSheet("background-color: green")

grid.addWidget(red, 0, 0)
grid.addWidget(blue, 0, 1)
grid.addWidget(green, 0, 2)
layout.addLayout(grid)

# нижняя панель
row3 = QHBoxLayout()
menu = QFrame()
menu.setFixedSize(500, 80)
menu.setStyleSheet("background-color: white")

menu_grid = QGridLayout(menu)

engine_RADAR_Navigation = QLabel("ENGINE   RADAR   NAVIGATION")
engine_RADAR_Navigation.setStyleSheet("color: black; font-size: 22px; border-radius: 10px;")


menu_grid.addWidget(engine_RADAR_Navigation, 0, 0)

row3.addWidget(menu)
row3.addWidget(QFrame())
layout.addLayout(row3)