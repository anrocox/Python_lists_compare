#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

How to compare two lists in python?

¿Como comparar dos listas en python?
'''

#create two lists equal
lista1, lista2 = [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
print (lista1 == lista2)

#create two different lists
lista1, lista2 = [1, 2, 3, 4], [1, 2, 3, 4, 5]
print (lista1 == lista2)

#create two lists equal, but unsorted.
lista1, lista2 = [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]
print (lista1 == lista2)

#order and compare
print (lista1.sort() == lista2.sort())
