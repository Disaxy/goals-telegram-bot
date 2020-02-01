# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from smiles import Smile


class Keyboard:

    back_btn = InlineKeyboardButton(
        text=Smile.back + ' Назад', callback_data='back')
    home_btn = InlineKeyboardButton(
        text=Smile.home + ' Домой', callback_data='home')

    def __init__(self, category_list: list):
        self.category = category_list

    def welcome(self):
        kb = InlineKeyboardMarkup(row_width=2)
        setting_btn = InlineKeyboardButton(
            text=Smile.settings + ' Настройки', callback_data='settings')
        goals_btn = InlineKeyboardButton(
            text=Smile.goals + ' Цели', callback_data='goals')
        diet_btn = InlineKeyboardButton(
            text=Smile.diet + ' Питание', callback_data='diet')
        sport_btn = InlineKeyboardButton(
            text=Smile.sport + ' Спорт', callback_data='sport')
        listen_btn = InlineKeyboardButton(
            text=Smile.listen + ' Чтение', callback_data='listen')
        regime_btn = InlineKeyboardButton(
            text=Smile.regime + ' Режим', callback_data='regime')
        budget_btn = InlineKeyboardButton(
            text=Smile.budget + ' Бюджет', callback_data='budget')
        water_btn = InlineKeyboardButton(
            text=Smile.water + ' Вода', callback_data='water')
        kb.add(goals_btn, regime_btn, diet_btn, water_btn, sport_btn,
               listen_btn, budget_btn, setting_btn)
        return kb

    def goals(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb

    def regime(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb

    def diet(self):
        kb = InlineKeyboardMarkup(row_width=2)
        calories_btn = InlineKeyboardButton(
            text=' Калории', callback_data='calories')
        kb.row(calories_btn)
        kb.add(self.back_btn)
        return kb

    def diet_calories(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.home_btn, self.back_btn)
        return kb

    def water(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb

    def sport(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb

    def listen(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb

    def budget(self):
        kb = InlineKeyboardMarkup(row_width=2)
        today_btn = InlineKeyboardButton(
            text=Smile.bugdet_today + ' За сегодня', callback_data='bugdet_today')
        month_btn = InlineKeyboardButton(
            text=Smile.budget_month + ' За месяц', callback_data='budget_month')
        expenses_btn = InlineKeyboardButton(
            text=Smile.budget_expenses + ' Последние траты', callback_data='budget_expenses')
        add_btn = InlineKeyboardButton(
            text=Smile.budget_add + ' Добавить', callback_data='budget_add')
        kb.row(expenses_btn)
        kb.add(today_btn, month_btn, add_btn, self.back_btn)
        return kb

    def budget_category(self):
        kb = InlineKeyboardMarkup(row_width=1)
        for cat in self.category:
            kb.add(InlineKeyboardButton(
                text=cat[0], callback_data=cat[0]))
        kb.row(self.home_btn, self.back_btn)
        return kb

    def budget_amount(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.home_btn, self.back_btn)
        return kb

    def budget_success(self):
        kb = InlineKeyboardMarkup(row_width=2)
        category_btn = InlineKeyboardButton(
            text=Smile.budget_category_change + ' Изменить категорию', callback_data='budget_add')
        budget_btn = InlineKeyboardButton(
            text=Smile.budget + ' Бюджет', callback_data='budget')
        kb.row(category_btn)
        kb.add(self.home_btn, budget_btn)
        return kb

    def settings(self):
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(self.back_btn)
        return kb
