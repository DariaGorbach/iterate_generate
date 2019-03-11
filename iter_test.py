# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:03:05 2019

@author: admin
"""
import unittest

from iter_gen import MyIterator

class IterTest(unittest.TestCase):
    
    
    def test_for_range_iterator(self):
        test_iteration = MyIterator(1,4,1)
        self.assertEqual(next(test_iteration), 0)
        self.assertRaises(StopIteration, next, test_iteration)
        test_list = list(MyIterator(1,4,1))
        range_fun = list(range(1,4,1))
        self.assertEqual(test_list, range_fun)
        
class GenTest(unittest.TestCase):
    
    
    def test_for_range_generator(self):
        test_generation = MyIterator.my_range(1,4,1)
        self.assertRaises(StopIteration, next, test_generation)
        test_list = list(MyIterator.my_range(1,4,1))
        range_fun = list(range(1,4,1))
        self.assertEqual(test_list, range_fun)
       
        
if __name__ == '__main__':
    unittest.main()
