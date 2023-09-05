# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='task_05.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)
WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')


def parse():
    parser = argparse.ArgumentParser(prog='get_data',
                                     description='Получение даты из строки',
                                     epilog='get_data("1-й четверг ноября")')
    parser.add_argument('-c', '--count', default=1, help='какой по счету день недели')
    parser.add_argument('-w', '--week_day', default=datetime.now().weekday(), help='какое название дня недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='какое название месяца')
    args = parser.parse_args()
    return get_data(f'{args.count} {args.week_day} {args.month}')


def get_data(data: str) -> datetime:
    try:
        count, week_day, month = data.split()
    except ValueError:
        logger.error(f'{data} не может быть разделена на компоненты')
        return None
    count = int(count[0])
    week_day = WEEK_DAYS.index(week_day[:3])
    month = MONTHS.index(month[:3]) + 1
    i = 0
    for day in range(1, 32):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == week_day:
            i += 1
            if i == count:
                return date


if __name__ == '__main__':
    print(parse())