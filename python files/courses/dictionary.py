# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:32:21 2019

@author: Ismail Bourbie
"""

my_dict = {"key1":"val1", "key2":"val2", "key3":"val3"} ## Create a Dictionary
my_dict['key1'] ## get the val associated to the key

### Dictionary Operations
my_dict['key4'] = 'val4' ## add an element at the end

"key3" in my_dict ## test if the key exist in dictionary
del(my_dict['key1']) ## remove an element
my_dict.keys() ## retutn keys
my_dict.values() ## return values