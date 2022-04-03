import unittest
from bissection import bissection
from fixPoint import fixPoint
from findZeroInterval import findZeroInterval
from newton import derivate, newtonMethod
import math

class TestBissection(unittest.TestCase):

    def test_1(self):
        self.assertAlmostEqual(
            bissection(
                lambda x: x + 1,
            -2, 1
            ), -1, 5
        )

    def test_2(self):
        self.assertEqual(
            bissection(
                lambda x: x + 1,
            -4, -2
            ), "Falhou"
        )

    def test_3(self):
        self.assertAlmostEqual(
            bissection(
                lambda x: x**2 - 4,
            0, 3
            ), 2, 5
        )

    def test_4(self):
        self.assertAlmostEqual(
            bissection(
                lambda x: math.sqrt(x) - math.cos(x),
            0, 1
            ), 0.6417143, 5
        )

    def test_5(self):
        self.assertAlmostEqual(
            bissection(
                lambda x: 3*(x+1)*(x-(1/2))*(x-1),
            -2, 1.5
            ), -1, 5
        )

    def test_6(self):
        self.assertAlmostEqual(
            bissection(
                lambda x: 3*(x+1)*(x-(1/2))*(x-1),
            -1.25, 2.5
            ), 1, 5
        )

class TestFixPoint(unittest.TestCase):

    def test_1(self):
        self.assertAlmostEqual(
            fixPoint(
                lambda x: 0.5, 0
            ), 0.5, 5
        )

    def test_2(self):
        self.assertEqual(
            fixPoint(
                lambda x: 1-x, 0
            ), "Falhou"
        )

    def test_3(self):
        self.assertAlmostEqual(
            fixPoint(
                lambda x: 3**(-x), 0
            ), 0.5478086, 5
        )

class TestFindZeroInterval(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            findZeroInterval(-97,
            lambda x: x, 5),
            [-2, 3]
        )

    def test_2(self):
        self.assertEqual(
            findZeroInterval(-100,
            lambda x: (x**3) - 5, 2),
            [0, 2]
        )

    def test_3(self):
        self.assertEqual(
            findZeroInterval(-100,
            lambda x: x - 10, 10),
            [1, 11]
        )

    def test_4(self):
        self.assertEqual(
            findZeroInterval(-1000,
            lambda x: (x**2) + 4, 10),
            "Falhou"
        )

    def test_5(self):
        self.assertEqual(
            findZeroInterval(-100,
            lambda x: (4**(x)) - 40, 10),
            [0, 10]
        )
        
class TestDerivate(unittest.TestCase):
    
    def test_1(self):
        self.assertAlmostEqual(
            derivate(0, lambda x: x**2 + x),
            1, 5
        )
        
    def test_2(self):
        self.assertAlmostEqual(
            derivate(1, lambda x: math.e**x),
            2.7182818, 5
        )
        
    def test_3(self):
        self.assertAlmostEqual(
            derivate(1, lambda x: math.log(x) + 10**x),
            24.0258509, 5
        )
        
class TestNewtonMethod(unittest.TestCase):
    
    def test_1(self):
        self.assertAlmostEqual(
            newtonMethod(math.pi/4, lambda x: math.cos(x) - x),
            0.7390851332, 5
        )
        
    def test_2(self):
        self.assertAlmostEqual(
            newtonMethod(-1, lambda x: math.sin(x) - x),
            0, 5
        )
        
    def test_3(self):
        self.assertAlmostEqual(
            newtonMethod(1, lambda x: x**2-4*x+4-math.log(x)),
            1.412391069, 5
        )
        
    def test_4(self):
        self.assertAlmostEqual(
            newtonMethod(2, lambda x: math.tan(x) - x + 4),
            2.04324495, 5
        )
