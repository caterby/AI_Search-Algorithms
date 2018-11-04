#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/23/18 5:15 PM
#@Author  :Jie Liu 
#@FileName: pancakepuzzle.py
#@Software: PyCharm

from puzzleconfig.pancakenode import pancakenode
import copy
import sys
import math
class pancakepuzzle(object):

     def __init__(self, filecontent, heuristicfunction = None):

         self.filecontent = filecontent
         self.allpancakenodes = []
         self.childnodes = []
         self.hn = heuristicfunction
         self.costtochild = 0
         self.pathcosttochild = dict()
         self.initialstate = list(eval(filecontent[1]))
         self.goalstate = list(eval(filecontent[2]))
         self.numberofpancakes = len(self.initialstate)
         
         self.addpancakenode(self.initialstate)
         self.addpancakenode(self.goalstate)
         self.initialnode = self.getpancakenode(self.initialstate)
         self.goalnode = self.getpancakenode(self.goalstate)

         for i in self.allpancakenodes:
             for child in i.childnodes:
                 print child.state

         


     def generatechildnodes(self, node):

         if (len(node.childnodes) == 0):
             newnode = []
             count = 0
             prevnode = copy.copy(node.state)

             for i in range(self.numberofpancakes):
                 w = i * -0.5
                 newnode = []
                 if (count == 0):
                     newnode = [(-1) * prevnode[count]] + prevnode[count + 1:]
                 elif (count < self.numberofpancakes):
                     newnode = [(-1) * prevnode[count]] + prevnode[0:count] + prevnode[count + 1:]
                 else:
                     newnode = [(-1) * prevnode[count]] + prevnode[0:count - 1]
                    
                 prevnode = newnode
                 count = count + 1

                 childnode = pancakenode(copy.copy(newnode))

                 if node.state != childnode.state:
                     childnode.parent = node
                     if childnode not in node.childnodes:
                        node.childnodes.append(childnode)
                        node.pathcosttochild[childnode] = w
         return node.childnodes


     def addpancakenode(self, state, isgoal = False):
         node = pancakenode(state, parent= None, isgoal=None)
         self.allpancakenodes.append(node)
         return self.allpancakenodes


     def getpancakenode(self, name):
         for node in self.allpancakenodes:
             if node.state == name:
                 return node

         return None


     def goaltest(self, testnode):
         if testnode.state == self.goalstate:
             return True
         else:
             return False

     def getpathcost(self, node):
         
         currentnode = self.initialnode
         pathcost = 0
         mincost = sys.maxint
         childnodelist = self.generatechildnodes(currentnode)
         
         for childnode in childnodelist:
             if mincost > currentnode.pathcosttochild[childnode]:
                 mincost = currentnode.pathcosttochild[childnode]
                 mincostnode = childnode
         currentnode = mincostnode
         
         if currentnode.state != node.state:
            pathcost += self.getpathcost(currentnode)
        
         return pathcost
                 

     def solution(self, node):
         path_back = []
         while node.state != self.initialstate:
             path_back.append(node)
             node = node.parent
         return list(reversed(path_back))


     def geteuclideandistance(self, node):

         squaresum = 0
         for i in range(len(self.initialstate)):
            squarevalue = pow((self.goalnode.state[i] - node.state[i]), 2)
            squaresum += squarevalue

         distance = math.sqrt(squaresum)

         return distance

     def getmanhattandistance(self, node):

         distance = 0
         for i in range(len(self.initialstate)):
            absvalue = abs(self.goalnode.state[i] - node.state[i])
            distance += absvalue

         return distance

     def getdotproductdistance(self, node):
         distance = 0
         for i in range(len(self.initialstate)):
             distance  += self.goalnode.state[i]*node.state[i]

         return distance
     
     def getcosinesimilarity(self, node):
         dotproduct = 0
         for i in range(len(self.initialstate)):
             dotproduct  += self.goalnode.state[i]*node.state[i]
             
         squaregoalmode = 0
         for i in range(len(self.initialstate)):
             squaregoalmode += pow(self.goalnode.state[i], 2)
         goalmode = math.sqrt(squaregoalmode)
         
         squarenodemode = 0
         for i in range(len(self.initialstate)):
             squarenodemode += pow(node.state[i], 2)
         nodemode = math.sqrt(squarenodemode)
         
         similarity = dotproduct / (goalmode*nodemode + 100)
         
         return similarity
     
     def getgapdistance(self, node):
         cost = 0
         for i in range(len(self.initialstate)):
             if i != len(self.initialstate) -1:
                 if abs(node.state[i] - node.state[i+1]) > 1:
                        cost += 1
                 else:
                    if abs(node.state[i] - self.goalnode.state[i] -1) > 1:
                        cost += 1
         return cost
     
       