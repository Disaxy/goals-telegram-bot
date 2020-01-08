# -*- coding: utf-8 -*-

from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from budget import category
from smiles import Smile


class Keyboard:

    @staticmethod
    def welcome():
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

    @staticmethod
    def goals():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def regime():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def diet():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def water():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def sport():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def listen():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def budget():
        kb = InlineKeyboardMarkup(row_width=2)
        add_btn = InlineKeyboardButton(
            text=Smile.budget_add + ' Добавить', callback_data='budget_add'
        )
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(add_btn, back_btn)
        return kb

    @staticmethod
    def budget_category():
        kb = InlineKeyboardMarkup(row_width=1)
        for cat in category:
            kb.add(InlineKeyboardButton(
                text=cat.name, callback_data=cat.name.replace(' ', '_')))
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def budget_amount():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def settings():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(
            text=Smile.back + ' Назад', callback_data='back')
        kb.add(back_btn)
        return kb
