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
