# This file is placed in the Public Domain.
# pylint: disable=C0113,C0114,C0115,C0116


import unittest


from gozerbot import Command, scan
from gozerbot.mod import irc


class TestScan(unittest.TestCase):

    def test_scan(self):
        scan(irc)
        self.assertTrue("cfg" in Command.cmd)
