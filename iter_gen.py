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
        current_num = self.start
        if self.start >= self.stop:
            raise StopIteration          
        else:
            current_num = self.start
            self.start += self.step
            return current_num
            
            
class MyGenerator:
        
    def my_range(start, stop, step):
        n = start
        while n < stop:
            yield n
            n += step


for current_num in MyIterator(1,9,1):
    print(current_num)    
    
        

                
