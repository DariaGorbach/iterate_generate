# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:17:41 2019

@author: admin
"""  

    
class MyIterator:
 
    
    def __iter__(self):
        return self
    
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __next__(self):
        self.current_num = self.start
        if self.current_num >= self.stop:
            raise StopIteration          
        self.current_num += self.step
        return self.current_num
        
    def my_range(self, start, stop, step):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


for current_num in MyIterator(1,9,1):
    print(current_num)    
    
        

                