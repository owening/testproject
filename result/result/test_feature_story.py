import allure
import pytest


@allure.feature("登陆模块")
class TestLogin():
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("登陆成功")
    def test_login_success(self):
        print("这是登陆： 测试用例，登陆成功")
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("登陆失败")
    def test_login_succes_a(self):
        print("这是登陆： 测试用例，登陆失败")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("用户名缺失")
    def test_login_succes_b(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        with allure.step("点击登陆之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass

if __name__ == '__main__':
    pytest.main()