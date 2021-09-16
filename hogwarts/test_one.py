import allure
import pytest

class TestCommon(object):
    def setup(self):
        pass

    def teardown(self):
        pass

    # @pytest.mark.skipif(reason="忽略我")
    @allure.feature("加法运算")
    @allure.story("场景1：两个整数相加")
    def test_add_case01(self):
        assert 1+1 == 2

    @allure.feature("加法运算")
    @allure.story("场景2：两个小数相加")
    def test_add_case02(self):
        assert 1.1 + 1.2 == 2.3

    @allure.feature("加法运算")
    @allure.story("场景3：整数和负数相加")
    def test_add_case03(self):
        assert -1 + 1 == 0


if __name__ == '__main__':
    pytest.main()