import allure
import pytest


class TestPayment:
    def test_pay_credit(self, setup):
        print("payment using credit")

    @pytest.mark.skip
    def test_pay_debit(self, setup):
        print("payment using debit")

    def test_pay_upi(self, setup):
        print("payment using upi")
        assert False
