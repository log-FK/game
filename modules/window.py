from PyQt6.QtWidgets import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QtWidgets, QFrame, QHBoxLayout,QVBoxLayout,QGridLayout, QLabel
from PyQt6.QtCore import QSize
from app import app

main_window = QMainWindow

primary_screen = app.primaryScreen()
screen_size = primary_screen.Size()

app.primaryScreen()
screen_size = primary_screen.size()

width_screen = screen_size.Width()
height_screen = screen_size.Height()

main_window = QMainWindow()
main_window.setGeometry(100, 100, 1024, 800)



main_frame = QFrame(parent= main_window)
main_frame.setStyleSheet("background-color:black")
main_frame.setFixedSize(100, 100)


main_layout = QHBoxLayout()

frame_layout = QVBoxLayout()
 
middle_layout = QHBoxLayout()



system_status_frame = QFrame(parent= main_frame)
system_status_frame.setStyleSheet("background-color: gray")
system_status_frame.setFixedSize(500,300)

status_layout = QVBoxLayout()
status_label = QLabel(parent= main_frame, text= "online")
status_label.setStyleSheet("font-size: 17px, font-weight: 700, color: white")



# system_status_frame.setLayout(status_layout)

status_layout.addWidget(status_label)
system_status_frame.setLayout(status_layout)

middle_layout.addWidget(system_status_frame)

frame_layout.addLayout(middle_layout)

bottom_grid = QGridLayout()




left_square_1 = QFrame(parent= main_frame)
left_square_1.setFixedSize(100, 100)
left_square_1.setStyleSheet("background-color: red")

middle_square_2 = QFrame(parent= main_frame)
middle_square_2.setFixedSize(100, 100)
middle_square_2.setStyleSheet("background-color: blue")


right_square_3 = QFrame(parent= main_frame)
right_square_3.setFixedSize(100, 100)
right_square_3.setStyleSheet("background-color: green")

# bottom_layout.addWidget(left_square_1)
# middle_layout.addWidget(middle_square_2)
# right_layout.addWidget(right_square_3)



    