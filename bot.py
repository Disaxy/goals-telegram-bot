# -*- coding: utf-8 -*-

import asyncio
import logging
import os
from configparser import ConfigParser
from exceptions import NotCorrectMessage

import uvloop
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils.executor import start_webhook
from aiogram.utils.markdown import bold, code, italic, pre, text

from budget import category
from google_sheet import SpreadSheet
from keyboards import Keyboard
from middlewares import AccessMiddleware
from smiles import Smile


config_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.cfg')
config = ConfigParser()
config.read(config_path)

API_TOKEN = config.get('TELEGRAM', 'API_TOKEN')
PROXY_URL = config.get('PROXY', 'URL')
WEBHOOK_HOST = config.get('WEBHOOK', 'HOST')
WEBAPP_HOST = config.get('APP', 'HOST')
WEBAPP_PORT = config.get('APP', 'PORT')
GOOGLESHEETS_FILE = config.get('GOOGLESHEETS', 'FILE')
GOOGLESHEETS_SPREADSHEET_ID = config.get('GOOGLESHEETS', 'SPREADSHEET_ID')
ADMIN = config.get('ADMIN', 'ID')

WEBHOOK_PATH = '/' + API_TOKEN
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

logging.basicConfig(level=logging.INFO)

uvloop.install()
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
dp.middleware.setup(AccessMiddleware(ADMIN))
spreadsheets = SpreadSheet(GOOGLESHEETS_FILE, GOOGLESHEETS_SPREADSHEET_ID)


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
    await message.reply(text=Smile.welcome + ' Мои привычки.', reply_markup=Keyboard().welcome(), reply=False)
    await Page.first()


@dp.message_handler(state=Page.budget_add, content_types=['text'])
async def send_message(message: types.Message, state: FSMContext):
    spreadsheets.append(message.text.split(' ')[0], message.text.split(' ')[1])
    await message.reply(text='Успешно добавлено!', reply=False)


@dp.callback_query_handler(state=Page.welcome)
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
        await callback.message.edit_text(text=Smile.regime + ' Мой режим дня.', reply_markup=Keyboard().regime())
        await Page.regime.set()

    if callback.data == 'budget':
        await callback.message.edit_text(text=Smile.budget + ' Мои расходы.', reply_markup=Keyboard().budget())
        await Page.budget.set()

    if callback.data == 'water':
        await callback.message.edit_text(text=Smile.water + ' Мой питьевой режим.', reply_markup=Keyboard().water())
        await Page.water.set()

    if callback.data == 'settings':
        await callback.message.edit_text(text=Smile.settings + ' Мои настройки.', reply_markup=Keyboard().settings())
        await Page.settings.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data != 'back', state=Page.budget)
async def budget_handler(callback: types.CallbackQuery):

    if callback.data == 'budget_add':
        await callback.message.edit_text(text='Выберите категорию.', reply_markup=Keyboard().budget_category())
        await Page.budget_add.set()

    await callback.answer()


@dp.callback_query_handler(state=Page.budget_add)
async def budget_add_handler(callback: types.CallbackQuery):

    if callback.data == 'back':
        await callback.message.edit_text(text=Smile.budget + ' Мои расходы.', reply_markup=Keyboard().budget())
        await Page.budget.set()
    else:
        for cat in category:
            if callback.data == cat.name.replace(' ', '_'):
                await callback.message.edit_text(text=cat.comment, reply_markup=Keyboard().budget_amount())
                await Page.budget_category.set()

    await callback.answer()


@dp.callback_query_handler(state=Page.budget_category)
async def budget_category_handler(callback: types.CallbackQuery):

    if callback.data == 'back':
        await callback.message.edit_text(text='Выберите категорию.', reply_markup=Keyboard().budget_category())
        await Page.budget_add.set()

    await callback.answer()


@dp.callback_query_handler(lambda callback: callback.data == 'back', state='*')
async def back_handler(callback: types.CallbackQuery):

    if callback.data == 'back':
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
