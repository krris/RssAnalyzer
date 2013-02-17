#!/usr/bin/python
# -*- coding: utf-8 -*-
import lexer
import urllib2
import parser
import sys
import tree
import operator
import codecs
import os

class Item:
    def __init__(self):
        self.title = []
        self.author = []
        self.link = []
        self.categories = []
        self.description = []
        self.searchQuality = 0

    def countSearchQuality(self, words):
        titleValue = 20
        authorValue = 20
        categoryValue = 5
        descriptionValue = 1
        quality = 0
        for word in words:
            quality += self.title.count(word) * titleValue
            quality += self.author.count(word) * authorValue
            quality += self.categories.count(word) * categoryValue
            quality += self.description.count(word) * descriptionValue
        self.searchQuality += quality

    def printItem(self):
        print "title: ", self.getTitle() 
        print "author: ", self.getAuthor()
        print "link: ", self.getLink()
        print "categories: ", self.getCategories()
        print "description: ", self.getDescription()
        print "searchQuality: ", item.searchQuality
        print "\n"
    
    def getTitle(self):
        return getString(self.title)

    def getAuthor(self):
        return getString(self.author)

    def getLink(self):
        link = ""
        for l in self.link:
            link += l
        return link

    def getCategories(self):
        return getString(self.categories)

    def getDescription(self):
        return getString(self.description)


def buildItems(root):
    items = []
    if root.tagName == "item":
        item = Item()
        item.node = root
        # search for "title", "link", ... in a parsing tree 
        # and using them initialize an item
        for child in item.node.children:
            if child.tagName == "title":
                item.title = child.content
            if child.tagName == "dc:creator":
                item.author = child.content
            if child.tagName == "link":
                item.link = child.content
            if child.tagName == "category":
                item.categories.extend(child.content)
            if child.tagName == "content:encoded":
                item.description = child.content
            elif child.tagName == "description":
                item.description = child.content
        # count quality of a current item
        item.countSearchQuality(words)
        items.append(item)
    for child in root.children:
        items.extend(buildItems(child))
    return items


def getString(list):
    string = ""
    for l in list:
        string += l + " "
    return string

def printResult(items):
    i = 1
    for item in items:
        print i, ") ", item.getTitle()
        print "searchQuality: ", item.searchQuality
        print item.getLink()
        print ""
        i += 1
   
# python search.py URL [words]
if __name__ == "__main__":
    url = sys.argv[1]    
    words = sys.argv[2:]
    response = urllib2.urlopen(url)
    lexer.initialize(response)    

    treeRoot = parser.program()
    if treeRoot == None:
        print "Parsing error"
        sys.exit()

    #tree.printTree(treeRoot)
    
    items = buildItems(treeRoot)
    items.sort(reverse=False, key = operator.attrgetter('searchQuality'))
    printResult(items)
