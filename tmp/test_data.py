import pytest
import yaml


class TestData:
    #参数化读取代码定义数据
   @pytest.mark.parametrize(("a","b"),[(10,20),(12,23),(15,27)])
   def test_data1(self,a,b):
       print(a + b)

  #参数化读取yaml文件数据
   @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./testdata.yaml")))
   def test_data2(self,a,b):
       b = 20
       print(a + b)




