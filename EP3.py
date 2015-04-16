# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:27:41 2015

@author: marcelotanak
"""
from IMC import IMC

ganso = open ("alimentos.csv", encoding = "latin1")
m1to = open ("usuario.csv", encoding = "utf-8")

pato = ganso.readlines ()
toloi = m1to.readlines ()

print (toloi [1])

info = toloi [1].split(",")

print (IMC (float(info [2]), float(info [4])*100, float(info[1])))






