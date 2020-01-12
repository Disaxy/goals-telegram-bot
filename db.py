# -*- coding: utf-8 -*-

import asyncio
from typing import NamedTuple

from aiosqlite import connect


class Expense(NamedTuple):
    category: str
    amount: int
    comment: str = None


class DB:

    def __init__(self, db_path):
        self.db_path = db_path

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
            await db.execute('INSERT INTO `expense` (category, amount, comment, date) VALUES (?, ?, ?, datetime("now", "localtime"))', (expense.category, expense.amount, expense.comment,))
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
    db = DB(db_path)
    # await db.create_expense(Expense(category='Питание', amount=100))
    # await db.remove_expense(5)
    # await db.remove_last_expense()
    # await db.view_expense()
    await db.last_day()

if __name__ == '__main__':
    asyncio.run(main())
