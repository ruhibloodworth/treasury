from datetime import datetime
from decimal import Decimal
from lark import Lark, Transformer

from treasury.entry import OpenEntry, TrEntry

class T(Transformer):
    pass
    YEAR = int
    MONTH = int
    DAY = int
    SIGNED_NUMBER = Decimal
    WORD = str
    def amount(self, args):
        return args[0]

    def date(self, args):
        return datetime(args[0], args[1], args[2])
    
    def account(self, args):
        return args[0]

    def open_entry(self, args):
        return OpenEntry(args[0],args[1], args[2])

    def tr_entry(self, args):
        return TrEntry(args[0], args[1], args[2], args[3])

    def start(self, args):
        return args

parser = Lark(r"""
    %ignore WS_INLINE

    start: [entry NEWLINE]* entry NEWLINE?

    ?entry: open_entry
          | tr_entry

    open_entry: date "OPEN" account amount
    tr_entry: date "TR" account account amount

    date: YEAR "-" MONTH "-" DAY
    YEAR: /[0-9]{4}/
    MONTH: /[0-9]{2}/
    DAY: /[0-9]{2}/

    account: WORD

    amount: SIGNED_NUMBER

    %import common.DIGIT
    %import common.NEWLINE
    %import common.SIGNED_NUMBER
    %import common.WORD
    %import common.WS_INLINE
""", transformer=T(), parser="lalr")
