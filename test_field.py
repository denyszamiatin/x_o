import pytest

import field as field_


@pytest.fixture
def field():
    return field_.Field()


def test_field_generation(field):
    assert str(field) == "   \n   \n   "


def test_get(field):
    assert field[0, 0] == ' '


def test_set(field):
    field[0, 0] = 'X'
    assert field[0, 0] == 'X'


def test_cell_occupied(field):
    field[0, 0] = 'X'
    with pytest.raises(ValueError) as e:
        field[0, 0] = 'X'
    assert "cell is occupied" in str(e.value)


def test_draw(field):
    for i in range(3):
        for j in range(3):
            field[i, j] = 'X'
    assert field.is_draw() == True


def test_win_in_row(field):
    field[0, 0] = 'X'
    field[0, 1] = 'X'
    field[0, 2] = 'X'
    assert field.is_win("X") == True


def test_win_in_column(field):
    field[0, 0] = 'X'
    field[1, 0] = 'X'
    field[2, 0] = 'X'
    assert field.is_win("X") == True


def test_win_in_main_diag(field):
    field[0, 0] = 'X'
    field[1, 1] = 'X'
    field[2, 2] = 'X'
    assert field.is_win("X") == True


def test_win_in_side_diag(field):
    field[0, 2] = 'X'
    field[1, 1] = 'X'
    field[2, 0] = 'X'
    assert field.is_win("X") == True


def test_copy(field):
    field[0, 0] = 'X'
    field1 = field.copy()
    assert str(field) == str(field1)
