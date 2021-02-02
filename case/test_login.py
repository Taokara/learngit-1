
import unittest

class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass只执行一次")
    def setUp(self) -> None:
        print("setUp执行多次")

    def test_login1(self):
        print("中间的函数1")
    def test_login2(self):
        print("中间的函数2")

    def tearDown(self) -> None:
        print("teardown执行多次")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownClass只执行一次")

