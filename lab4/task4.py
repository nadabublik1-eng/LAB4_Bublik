
import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QSpinBox,
                             QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout)


class InputPanel(QWidget):
    message_sent = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.message = QLineEdit()
        self.message.setPlaceholderText("Текст повідомлення")
        self.button = QPushButton("Надіслати")
        self.feedback = QLabel("Оцінки ще немає")
        layout.addWidget(self.message)
        layout.addWidget(self.button)
        layout.addWidget(self.feedback)
        self.button.clicked.connect(self.send)

    def send(self):
        text = self.message.text().strip()
        if text:
            self.message_sent.emit(text)

    def show_rating(self, rating, message):
        self.feedback.setText(f"Оцінка «{message}»: {rating}")


class ResultPanel(QWidget):
    rating_sent = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        self.current_message = ""
        layout = QVBoxLayout(self)
        self.received = QLabel("Повідомлення ще не отримано")
        self.received.setWordWrap(True)
        self.rating = QSpinBox()
        self.rating.setRange(1, 5)
        self.button = QPushButton("Оцінити повідомлення")
        self.button.setEnabled(False)
        layout.addWidget(self.received)
        layout.addWidget(self.rating)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.send_rating)

    def show_message(self, message):
        self.current_message = message
        self.received.setText(f"Отримано: {message}")
        self.button.setEnabled(True)

    def send_rating(self):
        self.rating_sent.emit(self.rating.value(), self.current_message)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кастомні сигнали")
        self.setMinimumSize(600, 240)
        layout = QVBoxLayout(self)
        panels = QHBoxLayout()
        self.input_panel = InputPanel()
        self.result_panel = ResultPanel()
        panels.addWidget(self.input_panel)
        panels.addWidget(self.result_panel)
        layout.addLayout(panels)

        self.pause = QCheckBox("Призупинити передавання")
        self.status = QLabel("Передавання ввімкнено")
        layout.addWidget(self.pause)
        layout.addWidget(self.status)

        self.input_panel.message_sent.connect(self.result_panel.show_message)
        self.result_panel.rating_sent.connect(self.input_panel.show_rating)
        self.pause.toggled.connect(self.toggle_connection)

    def toggle_connection(self, paused):
        if paused:
            self.input_panel.message_sent.disconnect(self.result_panel.show_message)
            self.status.setText("Передавання вимкнено")
        else:
            self.input_panel.message_sent.connect(self.result_panel.show_message)
            self.status.setText("Передавання ввімкнено")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
