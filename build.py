import PyInstaller.__main__
from distutils.dir_util import copy_tree

MAIN_EXECUTABLE: str = 'main.py'

DATA_SRC: str = 'questions'
DATA_DST: str = 'dist/main/questions'


def make_executable(file: str) -> None:
    PyInstaller.__main__.run([
        f'{file}',
        '--windowed'
    ])


def copy_data() -> None:
    copy_tree(DATA_SRC, DATA_DST)


if '__main__' == __name__:
    make_executable(MAIN_EXECUTABLE)
    copy_data()
