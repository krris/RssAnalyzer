#!/usr/bin/python
# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self):
        self.tagName = ""
        self.attributes = []
        self.children = []
        self.content = []
        self.parent = None
    
    def addChild(self, node):
        self.children.append(node)
        node.parent = self

def printTree(root):
    printNode(root)
    for child in root.children:
        printTree(child)
    
def printNode(node):

    print "TagName:"
    print "{:<20} {}".format("", node.tagName) 
    print "Attributes:"
    if node.attributes != []:
        for attr in node.attributes:
            print "{:<20}({:<20} {})".format("", attr[0], attr[1])
    else:
        print "{:<20} {:<20}".format("", "Empty")
   
    print "TagContent:"
    if node.content != []:
        contentToPrint = ""
        for c in node.content:
            contentToPrint += c + " "
        print "{:<20} {:<20}".format("", contentToPrint)
    else:
        print "{:<20} {:<20}".format("", "Empty")
    print "\n"

