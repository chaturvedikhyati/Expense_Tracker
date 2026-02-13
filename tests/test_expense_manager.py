import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.expense_manager import (
    validate_date,
    validate_amount,
    validate_category
)


def test_validate_date_valid():
    assert validate_date("2026-01-01") == "2026-01-01"


def test_validate_date_invalid():
    with pytest.raises(ValueError):
        validate_date("01-01-2026")


def test_validate_amount_valid():
    assert validate_amount(250) == 250
    assert validate_amount(99.999) == 100.0


def test_validate_amount_invalid():
    with pytest.raises(ValueError):
        validate_amount(-50)


def test_validate_category_valid():
    assert validate_category(" food ") == "Food"


def test_validate_category_invalid():
    with pytest.raises(ValueError):
        validate_category("")