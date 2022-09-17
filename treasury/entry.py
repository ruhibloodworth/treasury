from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Entry:
    date: datetime
    

@dataclass(frozen=True)
class OpenEntry(Entry):
    account: str
    amount: Decimal


@dataclass(frozen=True)
class TrEntry(Entry):
    src: str
    dest: str
    amount: Decimal
