# -*- coding: utf-8 -*-

import asyncio
from typing import NamedTuple

from aiosqlite import connect
from asyncinit import asyncinit


class Expense(NamedTuple):
    category: str
    amount: int
    comment: str = None


@asyncinit
class DB:

    async def __init__(self, db_path, init_path):
        self.init_path = init_path
        self.db = await connect(db_path)
        await self.__check_db()

    async def __check_db(self):
        async with self.db.execute('SELECT name FROM `sqlite_master` WHERE type="table" AND name="expense"') as cursor:
            table_exists = await cursor.fetchall()
            if not table_exists:
                await self.__initialize()

    async def __initialize(self):
        with open(self.init_path, 'r', encoding='utf-8') as file:
            sql = file.read()

            await self.db.executescript(sql)
            await self.db.commit()

    async def close(self):
        await self.db.close()

    async def view_expense(self):
        async with self.db.execute('SELECT * FROM `expense`') as cursor:
                # print(await cursor.fetchall())
            async for row in cursor:
                print(row)

    async def last_day(self):
        async with self.db.execute('SELECT * FROM `expense` WHERE date > datetime("now", "localtime", "-1 day")') as cursor:
            async for row in cursor:
                print(row)

    async def create_expense(self, expense: Expense):
        await self.db.execute('INSERT INTO `expense` (category_id, amount, comment, created) VALUES ((SELECT id FROM `category` WHERE name = ?), ?, ?, datetime("now", "localtime"))', (expense.category, expense.amount, expense.comment,))
        await self.db.commit()

    async def remove_expense(self, expense_id: int):
        await self.db.execute('DELETE FROM `expense` WHERE id = ?', (expense_id,))
        await self.db.commit()

    async def remove_last_expense(self):
        await self.db.execute('DELETE FROM `expense` WHERE id = (SELECT id FROM `expense` ORDER BY id DESC LIMIT 1)')
        await self.db.commit()

    async def get_categories(self) -> list:
        async with self.db.execute('SELECT name, description FROM `category`') as cursor:
            return await cursor.fetchall()


async def main():
    import os
    db_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '.sqlite')
    init_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'init.sql')
    db = await DB(db_path, init_path)
    # await db.check_db()
    # await db.create_expense(Expense(category='Продукты', amount=100))
    # await db.remove_expense(5)
    # await db.remove_last_expense()
    # await db.view_expense()
    # await db.last_day()
    print(await db.get_categories())

if __name__ == '__main__':
    asyncio.run(main())
