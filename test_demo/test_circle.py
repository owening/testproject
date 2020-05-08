# try:
#     num1 = int(input("请输入一个除数"))
#     num2 = int(input("请输入一个被除数"))
#     print(num1 / num2)
# except ValueError:
#     print("这是一个异常")


class MyException(Exception):
    def __init__(self,value1,value2):
         self.value1=value1
         self.value2=value2

#调用自定义异常
raise MyException("value1","value2")
