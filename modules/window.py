from PyQt6.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel
from .app import app

window = QWidget()

screen_size = app.primaryScreen().size()
width = screen_size.width()
height = screen_size.height()

window.setGeometry(100, 100, width - 200, height - 200)

# Окно: чёрный фрейм на всё окно
main_layout = QHBoxLayout(window)
main_layout.setContentsMargins(0, 0, 0, 0)

main_frame = QFrame()
main_frame.setStyleSheet("background-color: black")
main_layout.addWidget(main_frame)

frame_layout = QVBoxLayout(main_frame)
frame_layout.setContentsMargins(10, 10, 10, 10)
frame_layout.setSpacing(10)

# --- Заголовок (сам займёт всё свободное место по высоте) ---
title_label = QLabel("SPACE CONTROL")
title_label.setStyleSheet("color: white; font-size: 28px;")
frame_layout.addWidget(title_label)

# --- Серый блок слева + распорка справа ---
middle_layout = QHBoxLayout()

system_status_frame = QFrame()
system_status_frame.setStyleSheet("background-color: gray")
system_status_frame.setFixedSize(500, 300)

# без layout: label остаётся в левом верхнем углу
status_label = QLabel("SYSTEM ONLINE", parent=system_status_frame)
status_label.setStyleSheet("color: white; font-size: 22px;")

middle_layout.addWidget(system_status_frame)
middle_layout.addWidget(QFrame())  # распорка

frame_layout.addLayout(middle_layout)

# --- Цветные квадраты: распорки между ними растягиваются поровну ---
def make_square(color):
    square = QFrame()
    square.setFixedSize(100, 100)
    square.setStyleSheet(f"background-color: {color}")
    return square

squares_layout = QHBoxLayout()
squares_layout.addWidget(QFrame())
squares_layout.addWidget(make_square("red"))
squares_layout.addWidget(QFrame())
squares_layout.addWidget(make_square("blue"))
squares_layout.addWidget(QFrame())
squares_layout.addWidget(make_square("green"))
squares_layout.addWidget(QFrame())

frame_layout.addLayout(squares_layout)

# --- Белая полоса слева + распорка справа ---
bottom_layout = QHBoxLayout()

bottom_frame = QFrame()
bottom_frame.setStyleSheet("background-color: white")
bottom_frame.setFixedSize(500, 80)

bottom_text_label = QLabel("ENGINE        RADAR        NAVIGATION", parent=bottom_frame)
bottom_text_label.setStyleSheet("color: black; font-size: 22px;")   

bottom_layout.addWidget(bottom_frame)
bottom_layout.addWidget(QFrame())  # распорка

frame_layout.addLayout(bottom_layout)