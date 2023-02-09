import unittest


class Test(unittest.TestCase):
    def test_split(self):
        s = 'wikipédia and google'
        self.assertEqual(s.split(), ['wikipédia', 'and', 'google'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(3)

