# This file is placed in the Public Domain.


import unittest


from gozerbot import Client


class MyClient(Client):

    gotcha = False

    def raw(self, txt):
        MyClient.gotcha = True


class TestClient(unittest.TestCase):

    def setUp(self):
        MyClient.gotcha = False

    def test_clienteneedsraw(self):
        with self.assertRaises(NotImplementedError):
            clt = Client()
            clt.raw("bla")

    def test_clienthasraw(self):
        clt = MyClient()
        clt.raw("txt")
        self.assertTrue(clt.gotcha)
