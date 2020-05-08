

import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown")
    print("最后关闭浏览器")

def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

if __name__ == '__main__':
    pytest.main()