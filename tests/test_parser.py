from decimal import Decimal
from lark import Tree, Token
from treasury.parser import parser


def test_parse_open_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04")
    assert tree == Tree('start', [
        Tree('open_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('amount', [Decimal('123.04')])])])


def test_parse_tr_ok():
    tree = parser.parse("2022-03-04 TR Checking Savings 123.04")
    assert tree == Tree('start', [
        Tree('tr_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('account', [Token('WORD', 'Savings')]),
            Tree('amount', [Decimal('123.04')])])])


def test_parse_entries_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04\n2022-03-04 TR Checking Savings 123.04")
    assert tree == Tree('start', [
        Tree('open_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('amount', [Decimal('123.04')])]),
        Token('NEWLINE', '\n'),
        Tree('tr_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('account', [Token('WORD', 'Savings')]),
            Tree('amount', [Decimal('123.04')])])
    ])


def test_parse_entries_newline_terminated_ok():
    tree = parser.parse("2022-03-04 OPEN Checking 123.04\n2022-03-04 TR Checking Savings 123.04\n")
    assert tree == Tree('start', [
        Tree('open_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('amount', [Decimal('123.04')])]),
        Token('NEWLINE', '\n'),
        Tree('tr_entry', [
            Tree('date', [2022, 3, 4]),
            Tree('account', [Token('WORD', 'Checking')]),
            Tree('account', [Token('WORD', 'Savings')]),
            Tree('amount', [Decimal('123.04')])]),
        Token('NEWLINE', '\n')
    ])