from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from .app import app

window = QWidget()

size = app.primaryScreen().size()
window.setGeometry(100, 100, size.width() - 200, size.height() - 200)

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

engine = QLabel("ENGINE")
engine.setStyleSheet("color: black; font-size: 22px;")

radar = QLabel("RADAR")
radar.setStyleSheet("color: black; font-size: 22px;")

navigation = QLabel("NAVIGATION")
navigation.setStyleSheet("color: black; font-size: 22px;")

menu_grid.addWidget(engine, 0, 0)
menu_grid.addWidget(radar, 0, 1)
menu_grid.addWidget(navigation, 0, 2)

row3.addWidget(menu)
row3.addWidget(QFrame())
layout.addLayout(row3)