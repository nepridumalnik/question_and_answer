from window import Window

from PyQt5.QtWidgets import QApplication


if '__main__' == __name__:
    try:
        app: QApplication = QApplication([])

        w: Window = Window(None)
        w.setWindowTitle('Вопрос-ответ')
        w.show()

        exit(app.exec())
    except Exception as e:
        print(e)
        exit(-1)
