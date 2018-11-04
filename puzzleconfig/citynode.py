#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:11 PM
#@Author  :Jie Liu 
#@FileName: citynode.py
#@Software: PyCharm

class citynode(object):

    def __init__(self, state, location, parent, isgoal = False):

       self.state = state
       self.parent = parent
       self.location = location
       self.childnodes = []
       self.isgoal = isgoal
       self.pathcosttochild = dict()
       self.bestcosttochild = 0
       self.pathcost = 0
       self.totalpathcost = 0


    def getnode(self):
        return self.state


    def getlocation(self):
        return self.location


    def goaltest(self):
        return self.isgoal


    def getcosttochild(self, child):
        if child is not None:
            return self.getcosttochild(child)
        else:
            return None