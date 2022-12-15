from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QTextBrowser

from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextOption

import os.path


# Контейнер с вопросом
class Question:
    question: str = 'q'
    answer: str = 'a'

    def __init__(self, path: str) -> None:
        '''
        Загружаем вопросы с ответами
        '''

        q: str = path + '/' + self.question
        if not os.path.isfile(q):
            raise f'Отсутствует вопрос {q}'
        a: str = path + '/' + self.answer
        if not os.path.isfile(a):
            raise f'Отсутствует ответ {a}'

        with open(q, 'r') as f:
            self.question_text = f.read()
        with open(a, 'r') as f:
            self.answer_text = f.read()


# Окно со списком вопросов и ответов
class Window(QWidget):
    def __init__(self, parent: QWidget = None, path: str = os.path.dirname(os.path.abspath(__file__)) + '/' + 'questions') -> None:
        if not os.path.isdir(path):
            raise f'Отсутствует директория {self.path}'

        super().__init__(parent)

        self.__get_questions(path)
        self.__setup_ui()

    def __get_questions(self, path: str) -> None:
        '''
        Получить вопросы с ответами
        '''

        self.questions: list[Question] = []
        for dir in next(os.walk(path))[1]:
            try:
                q: Question = Question(path + '/' + dir)
                self.questions.append(q)
            except Exception as e:
                print(e)

        self.current_questions = self.questions

    def __update_questions(self) -> None:
        '''
        Обновление списка вопросов
        '''

        self.questionsList.clear()
        for question in self.current_questions:
            self.questionsList.addItem(question.question_text)

    def __setup_ui(self) -> None:
        '''
        Настройка интерфейса        
        '''

        font: QFont = QFont('Arial', 14)
        self.setFont(font)

        self.setMinimumWidth(950)
        self.setMinimumHeight(700)

        layout: QHBoxLayout = QHBoxLayout(self)

        self.questionsList: QListWidget = QListWidget(self)
        self.questionsList.setWordWrap(True)

        search_input: QLineEdit = QLineEdit(self)
        search_input.setPlaceholderText('Поиск')

        question_layout: QVBoxLayout = QVBoxLayout()
        question_layout.addWidget(self.questionsList)
        question_layout.addWidget(search_input)

        self.answer: QTextBrowser = QTextBrowser(self)
        self.answer.setReadOnly(True)
        self.answer.setWordWrapMode(QTextOption.WordWrap)

        layout.addLayout(question_layout)
        layout.addWidget(self.answer)

        self.__update_questions()

        self.questionsList.currentRowChanged.connect(self.__on_item_clicked)
        search_input.textChanged.connect(self.__on_search_text_changed)

    def __on_item_clicked(self, index: int):
        '''
        Обработка нажатия на элемент
        '''

        self.answer.setPlainText(self.current_questions[index].answer_text)

    def __on_search_text_changed(self, text: str) -> None:
        '''
        Применение нового фильтра поиска
        '''

        self.current_questions = []

        for question in self.questions:
            if self.__contains_strings(text.split(' '), question.question_text):
                self.current_questions.append(question)

        self.__update_questions()

    def __contains_strings(self, words: list[str], text_to_check: str) -> bool:
        '''
        Проверка на содержание одного из слов нового фильтра
        '''

        text_to_check: str = text_to_check.lower()
        for word in words:
            if word.lower() in text_to_check:
                return True

        return False
