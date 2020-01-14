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
        self.db_path = db_path
        self.init_path = init_path
        await self.__check_db()
    
    async def __check_db(self):
        async with connect(self.db_path) as db:
            async with db.execute('SELECT name FROM `sqlite_master` WHERE type="table" AND name="expense"') as cursor:
                table_exists = await cursor.fetchall()
                if not table_exists:
                    await self.__initialize()

    async def __initialize(self):
        with open(self.init_path, 'r', encoding='utf-8') as file:
            sql = file.read()

        async with connect(self.db_path) as db:
            await db.executescript(sql)
            await db.commit()

    async def view_expense(self):
        async with connect(self.db_path) as db:
            async with db.execute('SELECT * FROM `expense`') as cursor:
                # print(await cursor.fetchall())
                async for row in cursor:
                    print(row)

    async def last_day(self):
        async with connect(self.db_path) as db:
            async with db.execute('SELECT * FROM `expense` WHERE date > datetime("now", "localtime", "-1 day")') as cursor:
                async for row in cursor:
                    print(row)

    async def create_expense(self, expense: Expense):
        async with connect(self.db_path) as db:
            await db.execute('INSERT INTO `expense` (category_id, amount, comment, created) VALUES ((SELECT id FROM `category` WHERE name = ?), ?, ?, datetime("now", "localtime"))', (expense.category, expense.amount, expense.comment,))
            await db.commit()

    async def remove_expense(self, expense_id: int):
        async with connect(self.db_path) as db:
            await db.execute('DELETE FROM `expense` WHERE id = ?', (expense_id,))
            await db.commit()

    async def remove_last_expense(self):
        async with connect(self.db_path) as db:
            await db.execute('DELETE FROM `expense` WHERE id = (SELECT id FROM `expense` ORDER BY id DESC LIMIT 1)')
            await db.commit()


async def main():
    import os
    db_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '.sqlite')
    init_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'init.sql')
    db = await DB(db_path, init_path)
    # await db.check_db()
    await db.create_expense(Expense(category='Продукты', amount=100))
    # await db.remove_expense(5)
    # await db.remove_last_expense()
    await db.view_expense()
    # await db.last_day()

if __name__ == '__main__':
    asyncio.run(main())
