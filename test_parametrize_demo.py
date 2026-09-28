import pytest

@pytest.mark.parametrize("text, expected", [
    ("hello", "HELLO"),
    ("", ""),
    ("Привіт", "ПРИВІТ"),
    ("123", "123"),
])
def test_upper(text, expected):
    assert text.upper() == expected
