# -*- coding: utf-8 -*-

from typing import NamedTuple, List, Dict


class Message(NamedTuple):
    category: str
    amount: int
    comment: str
