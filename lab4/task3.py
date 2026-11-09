
import sys
from pathlib import Path
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QToolBar,
                             QFileDialog, QMessageBox)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовий редактор")
        self.resize(600, 400)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Введіть текст")
        self.setCentralWidget(self.editor)

        open_action = QAction("Відкрити", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Зберегти", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)

        about_action = QAction("Про програму", self)
        about_action.triggered.connect(self.about)

        qt_action = QAction("Про Qt", self)
        qt_action.triggered.connect(self.about_qt)

        file_menu = self.menuBar().addMenu("Файл")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        help_menu = self.menuBar().addMenu("Довідка")
        help_menu.addAction(about_action)
        help_menu.addAction(qt_action)

        toolbar = QToolBar("Інструменти", self)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        self.addToolBar(toolbar)

        self.statusBar().showMessage("Символів: 0")
        self.editor.textChanged.connect(self.update_status)

    def update_status(self):
        self.statusBar().showMessage(
            f"Символів: {len(self.editor.toPlainText())}"
        )

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Відкрити файл", "", "Текстові файли (*.txt);;Усі файли (*)"
        )
        if path:
            try:
                self.editor.setPlainText(Path(path).read_text(encoding="utf-8"))
                self.statusBar().showMessage(f"Відкрито: {path}")
            except (OSError, UnicodeError) as error:
                QMessageBox.warning(self, "Помилка", str(error))

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Зберегти файл", "", "Текстові файли (*.txt);;Усі файли (*)"
        )
        if path:
            try:
                Path(path).write_text(self.editor.toPlainText(), encoding="utf-8")
                self.statusBar().showMessage(f"Збережено: {path}")
            except OSError as error:
                QMessageBox.warning(self, "Помилка", str(error))

    def about(self):
        QMessageBox.about(self, "Про програму", "Простий текстовий редактор PyQt6.")

    def about_qt(self):
        QMessageBox.aboutQt(self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
