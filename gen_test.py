# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:09:33 2019

@author: admin
"""

import unittest

from iter_gen import MyGenerator

class GenTest(unittest.TestCase):
    
    def test_for_range_generator(self):
        test_generation = MyGenerator.my_range(1,4,1)
        with self.assertRaises(StopIteration):
            next(test_generation)
            next(test_generation)
            next(test_generation)
            next(test_generation)
        test_list = list(MyGenerator.my_range(1,4,1))
        range_fun = list(range(1,4,1))
        self.assertEqual(test_list, range_fun)
        

if __name__ == '__main__':
   unittest.main()