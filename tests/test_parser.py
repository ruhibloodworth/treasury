from datetime import datetime
from decimal import Decimal
from lark import Tree, Token

from treasury.entry import OpenEntry, TrEntry
from treasury.parser import parser


def test_parse_open_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04")
    assert tree == [OpenEntry(datetime(2022,3,4), "Checking", Decimal('123.04'))]


def test_parse_tr_ok():
    tree = parser.parse("2022-03-04 TR Checking Savings 123.04")
    assert tree == [TrEntry(datetime(2022,3,4), "Checking", "Savings", Decimal('123.04'))]


def test_parse_entries_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04\n2022-03-04 TR Checking Savings 123.04")
    assert tree == [
        OpenEntry(datetime(2022,3,4), "Checking", Decimal('123.04')),
        Token('NEWLINE', '\n'),
        TrEntry(datetime(2022,3,4), "Checking", "Savings", Decimal('123.04'))
    ]


def test_parse_entries_newline_terminated_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04\n2022-03-04 TR Checking Savings 123.04\n")
    assert tree == [
        OpenEntry(datetime(2022,3,4), "Checking", Decimal('123.04')),
        Token('NEWLINE', '\n'),
        TrEntry(datetime(2022,3,4), "Checking", "Savings", Decimal('123.04')),
        Token('NEWLINE', '\n')
    ]