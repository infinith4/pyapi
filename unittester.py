import unittest
# unittest.TestCaseの子クラスを作成します
class MyTest(unittest.TestCase):

    # メソッド名は必ず「test」をプレフィックスに付けます
    def test_do_something(self):
        # 検証を行います
        one = 1
        self.assertEqual(one, 1, "one is 1")