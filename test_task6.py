from unittest import TestCase
import test6


class TestPrime (TestCase):

    def test_revers(self):
        self.assertEqual(test6.revers("flamingo axe"), "ognimalf exa")
