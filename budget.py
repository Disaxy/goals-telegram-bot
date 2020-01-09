# -*- coding: utf-8 -*-

from typing import Dict, List, NamedTuple
from smiles import Smile


class Message(NamedTuple):
    category: str
    amount: int
    comment: str


class Category(NamedTuple):
    name: str
    comment: str


category = [
    Category(name=Smile.budget_category_eatout + ' Еда вне дома',
             comment=Smile.budget_category_eatout + ' Бизнес ланчи, перекусы, кофе с собой'),
    Category(name=Smile.budget_category_products + ' Продукты',
             comment=Smile.budget_category_products + ' Покупки в супермаркетах и рынках'),
    Category(name=Smile.budget_category_restaurants + ' Бары и рестораны',
             comment=Smile.budget_category_restaurants + ' Бары, рестораны, кафе, кальянные, бургерные'),
    Category(name=Smile.budget_category_transport + ' Транспорт',
             comment=Smile.budget_category_transport + ' Общественный транспорт, такси'),
    Category(name=Smile.budget_category_gifts + ' Подарки',
             comment=Smile.budget_category_gifts + ' Дни рождения, свадьбы, коллегам, мат. помощь'),
    Category(name=Smile.budget_category_health + ' Здоровье',
             comment=Smile.budget_category_health + ' Мед услуги, средства гигиены, лекарства, спорт'),
    Category(name=Smile.budget_category_clothes + ' Одежда',
             comment=Smile.budget_category_clothes + ' Покупка одежды, уход, химчистка'),
    Category(name=Smile.budget_category_entertainment + ' Развлечения',
             comment=Smile.budget_category_entertainment + ' Кино, театры, музеи'),
    Category(name=Smile.budget_category_regular + ' Регулярные',
             comment=Smile.budget_category_regular + ' Подписки на сервисы, мобильная связь, интернет'),
    Category(name=Smile.budget_category_others + ' Прочее',
             comment=Smile.budget_category_others + ' Все остальное')
]
