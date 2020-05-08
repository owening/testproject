import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境,对应的IP是:",env["test"])
        elif "deb" in env:
         print("这是开发环境,对应的IP是:",env["dev"])