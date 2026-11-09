
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QDialog, QDialogButtonBox,
                             QFormLayout, QVBoxLayout, QLabel, QLineEdit,
                             QPushButton, QInputDialog, QMessageBox)


QSS = """
QWidget { background-color: #f4f6fb; }
QLabel { color: #26374a; font-size: 13px; }
QPushButton { background-color: #d8e5fa; border: 1px solid #789bd0;
              border-radius: 5px; padding: 7px; }
QPushButton:hover { background-color: #b8d0f5; }
QLineEdit { background-color: white; border: 1px solid #9caec4;
            border-radius: 4px; padding: 5px; }
QLineEdit:focus { border: 2px solid #4169b1; }
QLabel#resultLabel { color: #1650a4; font-weight: bold; }
"""


class UserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Дані користувача")
        layout = QVBoxLayout(self)
        form = QFormLayout()
        self.name = QLineEdit()
        self.email = QLineEdit()
        form.addRow("Ім'я:", self.name)
        form.addRow("Email:", self.email)
        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_data(self):
        return self.name.text(), self.email.text()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Діалоги та QSS")
        self.setMinimumSize(420, 240)
        layout = QVBoxLayout(self)

        self.result = QLabel("Дані не введено")
        self.result.setObjectName("resultLabel")
        self.result.setWordWrap(True)
        layout.addWidget(self.result)

        input_button = QPushButton("Ввести назву")
        input_button.clicked.connect(self.input_dialog)
        layout.addWidget(input_button)

        user_button = QPushButton("Дані користувача")
        user_button.clicked.connect(self.user_dialog)
        layout.addWidget(user_button)

        clear_button = QPushButton("Очистити")
        clear_button.clicked.connect(self.confirm_clear)
        layout.addWidget(clear_button)

    def input_dialog(self):
        text, ok = QInputDialog.getText(self, "Введення", "Назва:")
        if ok:
            self.result.setText(f"Назва: {text}")

    def user_dialog(self):
        dialog = UserDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name, email = dialog.get_data()
            self.result.setText(f"Ім'я: {name}; Email: {email}")

    def confirm_clear(self):
        answer = QMessageBox.question(
            self, "Підтвердження", "Очистити дані?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.result.setText("Дані не введено")


plain = "--plain" in sys.argv
app = QApplication([sys.argv[0]])
if not plain:
    app.setStyleSheet(QSS)
window = Window()
window.show()
sys.exit(app.exec())
