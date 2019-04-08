# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:06:18 2019

@author: Ismail Bourbie
"""

l = [1,2,3, 5, 6, 7] ## create list
type(l) ## list
l[0] ## get value at an index
l[0:4] ## slice a list
l[0] = 0 ## list are like tuples but mutable (you can change values inside list)

## iterate list (sum of list elements)
total = 0
for i in l:
    total += i
print(total)

## List Operations
l.append(8) ## add 8 at the end
l2 = l + [9, 10] ## concatenate two lists
l.extend([9, 10]) ## extend a list by add elements of list at the end
l.remove(2) ## remove the first element of value 2 (not the index)
del(l[0]) ## remove element at specific index
l.pop() ## remove element at the end of list
list("abc") ## convert string to list eg: ["a", "b", "c"]
"hello, world!".split(",") ## return ["hello", " world!"]
"_".join(["a", "b", "c"]) ## join element (must be strings element) of l with eg: '_' char
l.sort() ## sort a list
l.reverse() ## reverse a list
l.index(2) ## return the index of element 2
l.count(2) ## count the number of element in list 
l.insert(0, 100) ## insert 100 index 0

## Example of cloning and aliasing
numbers1 = [1, 2, 3]
numbers2 = numbers1
numbers3 = numbers1[:] ## clone numbers1
numbers1.append(4) ## this will add also a 4 to numbers2





