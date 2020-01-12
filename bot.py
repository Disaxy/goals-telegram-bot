# -*- coding: utf-8 -*-

import asyncio
import logging
import os
from configparser import ConfigParser
from exceptions import NotCorrectMessage

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.files import PickleStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils.executor import start_webhook
from aiogram.utils.markdown import bold, code, italic, pre, text

from budget import category
from google_sheet import SpreadSheet, Calendar
from keyboards import Keyboard
from middlewares import AccessMiddleware
from smiles import Smile

fsm_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.data')
config_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.cfg')
config = ConfigParser()
config.read(config_path)

API_TOKEN = config.get('TELEGRAM', 'API_TOKEN')
PROXY_URL = config.get('PROXY', 'URL')
WEBHOOK_HOST = config.get('WEBHOOK', 'HOST')
WEBAPP_HOST = config.get('APP', 'HOST')
WEBAPP_PORT = config.get('APP', 'PORT')
GOOGLE_FILE = config.get('GOOGLE', 'FILE')
GOOGLE_SPREADSHEET_ID = config.get('GOOGLE', 'SPREADSHEET_ID')
ADMIN = config.get('ADMIN', 'ID')

WEBHOOK_PATH = '/' + API_TOKEN
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

logging.basicConfig(level=logging.INFO)

storage = PickleStorage(fsm_path)
bot = Bot(token=API_TOKEN, proxy=PROXY_URL, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(bot=bot, storage=storage)
dp.middleware.setup(AccessMiddleware(ADMIN))
spreadsheets = SpreadSheet(GOOGLE_FILE, GOOGLE_SPREADSHEET_ID)
calendar = Calendar(GOOGLE_FILE)


class Page(StatesGroup):
    welcome = State()
    goals = State()
    diet = State()
    sport = State()
    listen = State()
    regime = State()
    budget = State()
    budget_add = State()
    budget_category = State()
    water = State()
    settings = State()


@dp.message_handler(state='*', commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(text=text(Smile.welcome + ' Мои привычки'), reply_markup=Keyboard().welcome())
    await Page.first()


@dp.message_handler(state=Page.budget_category, content_types=['text'])
async def send_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        category = data.get('category')
        amount = message.text.split(' ')[0]
        comment = ' '.join(message.text.split(' ')[1:])

    spreadsheets.append(category=category, amount=amount, comment=comment)

    await message.answer(text=text('Успешно добавлено ' + bold(amount) + ' рублей в категорию ' + bold(category), 'Вы можете продолжать добавлять расходы в эту категорию или выбрать другую.', sep='\n\n'), reply_markup=Keyboard().budget_success())


@dp.callback_query_handler(lambda callback: callback.data not in ['home', 'back', 'budget_add'], state=[Page.welcome, Page.budget_category])
async def welcome_handler(callback: types.CallbackQuery):

    if callback.data == 'goals':
        await callback.message.edit_text(text=Smile.goals + ' Мои цели.', reply_markup=Keyboard().goals())
        await Page.goals.set()

    if callback.data == 'diet':
        await callback.message.edit_text(text=Smile.diet + ' Мое питание.', reply_markup=Keyboard().diet())
        await Page.diet.set()

    if callback.data == 'sport':
        await callback.message.edit_text(text=Smile.sport + ' Мои тренировки.', reply_markup=Keyboard().sport())
        await Page.sport.set()

    if callback.data == 'listen':
        await callback.message.edit_text(text=Smile.listen + ' Мои книги.', reply_markup=Keyboard().listen())
        await Page.listen.set()

    if callback.data == 'regime':
        calendar.view()
        await callback.message.edit_text(text=Smile.regime + ' Мой режим дня.', reply_markup=Keyboard().regime())
        await Page.regime.set()

    if callback.data == 'budget':
        status = spreadsheets.view()
        await callback.message.edit_text(text=text(bold(Smile.budget + ' Мои расходы'), code('\n'.join(status)), sep='\n\n'), reply_markup=Keyboard().budget())
        await Page.budget.set()

    if callback.data == 'water':
        await callback.message.edit_text(text=Smile.water + ' Мой питьевой режим.', reply_markup=Keyboard().water())
        await Page.water.set()

    if callback.data == 'settings':
        await callback.message.edit_text(text=Smile.settings + ' Мои настройки.', reply_markup=Keyboard().settings())
        await Page.settings.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data not in ['back', 'home', 'budget'], state=[Page.budget, Page.budget_category])
async def budget_handler(callback: types.CallbackQuery):

    if callback.data == 'budget_add':
        await callback.message.edit_text(text='Выберите категорию.', reply_markup=Keyboard().budget_category())
        await Page.budget_add.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data != 'home', state=Page.budget_add)
async def budget_add_handler(callback: types.CallbackQuery, state: FSMContext):

    if callback.data == 'back':
        await callback.message.edit_text(text=Smile.budget + ' Мои расходы.', reply_markup=Keyboard().budget())
        await Page.budget.set()
    else:
        for cat in category:
            if callback.data == cat.name:
                await callback.message.edit_text(text=text(bold(cat.comment), 'Введите сумму которую потратили и  комментарий (не обязательно).', code('Пример: 100 бутылка воды'), sep='\n\n'), reply_markup=Keyboard().budget_amount())

                async with state.proxy() as data:
                    data['category'] = cat.name[2:]

                await Page.budget_category.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data != 'home', state=Page.budget_category)
async def budget_category_handler(callback: types.CallbackQuery):

    if callback.data == 'back':
        await callback.message.edit_text(text='Выберите категорию.', reply_markup=Keyboard().budget_category())
        await Page.budget_add.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data in ['back', 'home'], state='*')
async def back_handler(callback: types.CallbackQuery):

    if callback.data in ['back', 'home']:
        await callback.message.edit_text(text=Smile.welcome + ' Мои привычки.', reply_markup=Keyboard().welcome())
        await Page.first()
        await callback.answer()


async def on_startup(dp: Dispatcher):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp: Dispatcher):
    logging.warning('Shutting down..')

    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
