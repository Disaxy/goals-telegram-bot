# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard:

    @staticmethod
    def welcome():
        kb = InlineKeyboardMarkup(row_width=2)
        setting_btn = InlineKeyboardButton(
            text='⚙️ Настройки', callback_data='settings')
        goals_btn = InlineKeyboardButton(text='🏆 Цели', callback_data='goals')
        diet_btn = InlineKeyboardButton(text='🥕 Питание', callback_data='diet')
        sport_btn = InlineKeyboardButton(text='🏂 Спорт', callback_data='sport')
        listen_btn = InlineKeyboardButton(
            text='📚 Чтение', callback_data='listen')
        regime_btn = InlineKeyboardButton(
            text='🛏 Режим', callback_data='regime')
        budget_btn = InlineKeyboardButton(
            text='💰 Бюджет', callback_data='budget')
        water_btn = InlineKeyboardButton(text='💦 Вода', callback_data='water')
        kb.add(goals_btn, regime_btn, diet_btn, water_btn, sport_btn,
               listen_btn, budget_btn, setting_btn)
        return kb

    @staticmethod
    def goals():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def regime():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def diet():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def water():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def sport():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def listen():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def budget():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb

    @staticmethod
    def settings():
        kb = InlineKeyboardMarkup(row_width=2)
        back_btn = InlineKeyboardButton(text='⬅️ Назад', callback_data='back')
        kb.add(back_btn)
        return kb
