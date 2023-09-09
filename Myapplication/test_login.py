import pytest


class TestClass():
    def test_simple(self):
        a = 1
        assert a == 1

    def test_boolean(self):
        assert True

    def test_string_upper(self):
        course = 'seleniumm'
        assert course.upper() == 'SELENIUM'

    def test_list(self):
        course = ['java', 'python', 'javascript']
        assert 'python' in course

    def test_string_lower(self):
        course = 'seleniumm'
        assert course.lower() == 'SELENIUM'
