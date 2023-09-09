import pytest


class TestSample:

    @pytest.fixture()
    def setup(self):
        print("Launching browser")
        yield
        print("close browser")

    def test_login(self, setup):
        print("login page")

    def test_search(self, setup):
        print("searching for books")

    def test_advance_search(self,setup):
        print("Didn't find book opting for advance search ")

    def test_cart(self):
        print("added to cart")
