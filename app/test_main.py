from unittest import mock
import pytest
from datetime import date


from app.main import outdated_products


list_of_products = [{"name": "salmon",
                     "expiration_date": date(2022, 2, 10),
                     "price": 600},
                    {"name": "chicken",
                     "expiration_date": date(2022, 2, 5),
                     "price": 120},
                    {"name": "duck",
                     "expiration_date": date(2022, 2, 1),
                     "price": 160}]


@pytest.mark.parametrize(
    "date_variant,result",
    [
        (date.today(), ["salmon", "chicken", "duck"]),
        (date(2022, 2, 5), ["duck"]),
        (date(2022, 2, 2), ["duck"]),
        (date(2021, 5, 20), [])
    ]
)
def test_different_date_variants(date_variant: object,
                                 result: list) -> None:
    with mock.patch("datetime.date") as product_verification:
        product_verification.today.return_value = date_variant
        assert outdated_products(list_of_products) == result
