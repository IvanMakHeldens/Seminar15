# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
from datetime import datetime
import logging

logging.basicConfig(filename='task_04.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)
WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')


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
    print(get_data('1-й четверг ноября'))