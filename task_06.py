# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
from pathlib import Path
import logging
import argparse

logging.basicConfig(filename='task_06.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extention, is_dir, parent_dir')


def read_dir(path: Path):
    for file in path.iterdir():
        f = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(f)
        if f.is_dir:
            read_dir(Path(f.parent_dir)/f.name)


if __name__ == '__main__':
    print(read_dir(Path('D:\\PYTHON\\Seminar15')))
