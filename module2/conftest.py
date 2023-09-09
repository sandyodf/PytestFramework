import pytest


@pytest.fixture()
def setup():
    print("Opening browser")
    yield
    print("Closing browser")
