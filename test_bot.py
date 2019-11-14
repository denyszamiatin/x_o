import field as field_
import bot as bot_

import pytest


@pytest.fixture
def field():
    return field_.Field()


@pytest.fixture
def bot():
    return bot_.Bot('X')


def test_opposite_char():
    assert bot_.opposite_char('X') == 'O'
    assert bot_.opposite_char('O') == 'X'


def test_bot_win(field, bot):
    field[0, 0] = 'X'
    field[1, 1] = 'X'
    assert bot.move(field) == (2, 2)


def test_bot_loss(field, bot):
    field[0, 0] = 'O'
    field[0, 1] = 'O'
    assert bot.move(field) == (0, 2)


def test_center(field, bot):
    assert bot.move(field) == (1, 1)


def test_corners(field, bot):
    field[1, 1] = 'O'
    assert bot.move(field) == (0, 0)