
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QSpinBox,
                             QComboBox, QCheckBox, QPushButton, QVBoxLayout,
                             QFormLayout, QHBoxLayout)


def validate(name, age, role, accepted):
    if not name.strip():
        return "Помилка: введіть ім'я."
    if not 16 <= age <= 100:
        return "Помилка: вік має бути від 16 до 100."
    if role == "Оберіть роль":
        return "Помилка: оберіть роль."
    if not accepted:
        return "Помилка: підтвердьте згоду."
    return "Дані введено правильно."


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Інтерактивна форма")
        self.setMinimumSize(420, 310)
        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("Ім'я")
        form.addRow("Ім'я:", self.name)

        self.age = QSpinBox()
        self.age.setRange(0, 120)
        form.addRow("Вік:", self.age)

        self.role = QComboBox()
        self.role.addItems(["Оберіть роль", "Студент", "Викладач"])
        form.addRow("Роль:", self.role)

        self.accepted = QCheckBox("Погоджуюся з умовами")
        form.addRow("Згода:", self.accepted)
        layout.addLayout(form)

        self.preview = QLabel("Ім'я: —; роль: Оберіть роль")
        self.age_label = QLabel("Вік: 0")
        self.accepted_label = QLabel("Згоду не надано")
        self.result = QLabel("Результат перевірки")
        for label in (self.preview, self.age_label, self.accepted_label, self.result):
            layout.addWidget(label)

        buttons = QHBoxLayout()
        self.submit = QPushButton("Підтвердити")
        self.reset = QPushButton("Скинути")
        buttons.addWidget(self.submit)
        buttons.addWidget(self.reset)
        layout.addLayout(buttons)

        self.name.textChanged.connect(self.update_preview)
        self.role.currentTextChanged.connect(self.update_preview)
        self.age.valueChanged.connect(
            lambda value: self.age_label.setText(f"Вік: {value}")
        )
        self.accepted.toggled.connect(
            lambda checked: self.accepted_label.setText(
                "Згоду надано" if checked else "Згоду не надано"
            )
        )
        self.submit.clicked.connect(self.check_form)
        self.reset.clicked.connect(self.reset_form)

    def update_preview(self, *_):
        self.preview.setText(
            f"Ім'я: {self.name.text() or '—'}; роль: {self.role.currentText()}"
        )

    def check_form(self):
        self.result.setText(validate(
            self.name.text(), self.age.value(),
            self.role.currentText(), self.accepted.isChecked()
        ))

    def reset_form(self):
        self.name.clear()
        self.age.setValue(0)
        self.role.setCurrentIndex(0)
        self.accepted.setChecked(False)
        self.result.setText("Результат перевірки")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
