
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QComboBox,
                             QSpinBox, QCheckBox, QSlider, QProgressBar,
                             QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QFormLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анкета користувача")
        self.setMinimumSize(450, 400)
        layout = QVBoxLayout(self)

        title = QLabel("Анкета користувача")
        title.setToolTip("Заголовок форми")
        layout.addWidget(title)

        form = QFormLayout()
        self.name = QLineEdit()
        self.name.setPlaceholderText("Введіть ім'я")
        form.addRow("Ім'я:", self.name)

        self.role = QComboBox()
        self.role.addItems(["Студент", "Викладач", "Гість"])
        self.role.setToolTip("Оберіть роль")
        form.addRow("Роль:", self.role)

        self.age = QSpinBox()
        self.age.setRange(1, 120)
        self.age.setValue(18)
        form.addRow("Вік:", self.age)

        self.notifications = QCheckBox("Отримувати повідомлення")
        self.notifications.setChecked(True)
        form.addRow("Сповіщення:", self.notifications)
        layout.addLayout(form)

        row = QHBoxLayout()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.setToolTip("Рівень зацікавленості")
        row.addWidget(self.slider)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(50)
        row.addWidget(self.progress)
        layout.addLayout(row)

        self.comment = QTextEdit()
        self.comment.setPlaceholderText("Коментар")
        layout.addWidget(self.comment)

        self.button = QPushButton("Показати дані")
        self.button.setToolTip("Відобразити введені дані")
        layout.addWidget(self.button)

        self.result = QLabel("Результат з'явиться тут")
        self.result.setWordWrap(True)
        self.result.setToolTip("Результат анкети")
        layout.addWidget(self.result)

        self.slider.valueChanged.connect(self.progress.setValue)
        self.button.clicked.connect(self.show_result)

    def show_result(self):
        self.result.setText(
            f"Ім'я: {self.name.text()}; роль: {self.role.currentText()}; "
            f"вік: {self.age.value()}; рівень: {self.slider.value()}%"
        )


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
