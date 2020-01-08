# -*- coding: utf-8 -*-

from typing import NamedTuple, List, Dict


class Message(NamedTuple):
    category: str
    amount: int
    comment: str


class Category(NamedTuple):
    name: str
    comment: str


category = [
    Category(name='Еда вне дома', comment='Бизнес ланчи, перекусы, кофе с собой'),
    Category(name='Продукты', comment='Покупки в супермаркетах и рынках'),
    Category(name='Бары и рестораны',
             comment='Бары, рестораны, кафе, кальянные, бургерные'),
    Category(name='Транспорт', comment='Общественный транспорт, такси'),
    Category(name='Подарки', comment='Дни рождения, свадьбы, коллегам, мат. помощь'),
    Category(name='Здоровье',
             comment='Мед услуги, средства гигиены, лекарства, спорт'),
    Category(name='Одежда', comment='Покупка одежды, уход, химчистка'),
    Category(name='Развлечения', comment='Кино, театры, музеи'),
    Category(name='Регулярные',
             comment='Подписки на сервисы, мобильная связь, интернет'),
    Category(name='Прочее', comment='Все остальное')
]
