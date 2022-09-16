from decimal import Decimal
from lark import Lark, Transformer


class T(Transformer):
    pass
    YEAR = int
    MONTH = int
    DAY = int
    SIGNED_NUMBER = Decimal


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
