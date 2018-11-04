#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:47:35 2018

@author: liujie
"""

import heapq
class iterablePQ:


    def __init__(self, initial, costfn = lambda node: node.pathcost):
        self.node = initial
        print("Initial node's state is:")
        print self.node.state
        self.heap = []
        self.states = {}
        self.costfn = costfn
        self.add(self.node)

    def add(self, node):
        cost = self.costfn(node)
        heapq.heappush(self.heap, (cost, node))
        self.states[node] = node.state

    def pop(self):
        (cost, node) = heapq.heappop(self.heap)
        self.states.pop(None, node.state)  # remove state
        return node

    def replace(self, node):
        if node.state not in self:
            raise ValueError('{} not there to replace'.format(node.state))
        for (i, (cost, old_node)) in enumerate(self.heap):
            if old_node.state == node.state:
                self.heap[i] = (self.costfn(node), node)
                heapq._siftdown(self.heap, 0, i)
                return

    def __contains__(self, state):
        return state in self.states

    def __len__(self):
        return len(self.heap)