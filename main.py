# -*- mode: python ; coding: utf-8 -*-

from window import Window

from PyQt5.QtWidgets import QApplication


if '__main__' == __name__:
    try:
        app: QApplication = QApplication([])

        w: Window = Window(None)
        w.setWindowTitle('Вопрос-ответ')
        w.show()

        app.exec()
    except Exception as e:
        print(e)
