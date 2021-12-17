
# class間各mothod可以互相呼叫，but， 1個class存一個檔
from db import Database  # 從檔案db載入Database這個class

# import db      如果載入整個module
# db.Database()   使用時須要加入db.xxxx 才能使用

class Tool:
    def __init__(self):
        print("")
        self.db = Database()

    def asdasdasd(self):
        self.db.inser_data()

t = Tool()        