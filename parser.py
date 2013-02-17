#!/usr/bin/python
# -*- coding: utf-8 -*-
import htmlentitydefs
import lexer
from token import Token
from tree import *

errorCounter = 0
rssTagStack = []
root = TreeNode()
root.tagName = "root"

def getToken():
	global token
	token = lexer.read()

def error(msg):
    position = lexer.position()
    print "\nError! Position: (%s, %s)" % (position[1], position[2])
    print "Error message: %s\n" % msg
          
    global errorCounter 
    errorCounter += 1

def found(tokenToCheck):
	if Token.equalType(token, tokenToCheck):
		return True
	return False

def consume(tokenToConsume):
    if found(tokenToConsume):
        #print "Found token: (", token.type, ",", token.content, ")"
        #print "Position: ", lexer.position()
        lastToken = token
        getToken()
        return lastToken
    else:
        error("Expected to find:\n" 
            + tokenToConsume.type
            + "\nbut found:"
            + token.type)

def replaceXmlHtmlEntity(text):
   # text = token.content
    if text[:2] == '&#':
        # char reference
        try:
            if text[:3] == '&#x':
                text = unichr(int(text[3:len(text)-1], 16))
            else:
                text = unichr(int(text[2:len(text)-1]))
        except ValueError:
            pass
    else:
       # named enitity
       try:
           text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
       except KeyError:
           pass
    #token.content = text
    return text.encode("utf-8")

def replaceSpecialChar(token):
    if token.content == "&amp;":
        token.content = "&"
    if token.content == "&lt;":
        token.content = "<"
    if token.content == "&gt;":
        token.content = ">"
    if token.content == "&apos;":
        token.content = "'"
    if token.content == "&quot;":
        token.content == '"'

# TagName = [ Namespace ':' ] ident
# Namespace = ident
def tagName():
    lastToken = consume(Token("ident"))
    tagName = lastToken.content
    if found(Token(":")):
        lastToken = consume(Token(":"))
        tagName += lastToken.content
        lastToken = consume(Token("ident"))
        tagName += lastToken.content

    return tagName

# AttrValue = any token without '"'
def attrValue():
    value = ""
    while True:
        if found(Token('"')):
            #print "attrValue: ", value
            return value
        else:
            value += token.content
            getToken()
    
# TagAttribute = [ Namespace ':'] ident '="' AttrValue '"'
# Namespace = ident
def tagAttribute():
    lastToken = consume(Token("ident"))
    attrName = lastToken.content
    if found(Token(":")):
        lastToken = consume(Token(":"))
        attrName += lastToken.content
        lastToken = consume(Token("ident"))
        attrName += lastToken.content
    consume(Token('="'))
    value = attrValue()
    consume(Token('"'))
    
    return (attrName, value)


# Text = every token without '<' '</' '>' '/>'
def text():
    if not found(Token("]]>")) or not found(Token("<")) or not found(Token("</")) or not found(Token(">")) or not found(Token("/>")):
        if found(Token('xmlHtmlEntity')):
            token.content = replaceXmlHtmlEntity(token.content)

        lastToken = token
        getToken()
        return lastToken.content
    
# CdataContent = Text {HtmlTag | Text}
def cdataContent():
    content = []
    textContent = text()

    # check if Text is empty
    if textContent != None:
        content.append(textContent)
    else:
        return content
    while True:
        # if a token belongs to the end of Cdata, 
        # i.e '<![' 'CDATA' '[' {CdataContent} ']]>'
        if found(Token("]]>")):
            return content 
        # if a token is in the beginning of HtmlTag
        elif found(Token("<")) or found(Token("</")):
            htmlTag()
        else:
            content.append(text())
    return content

# HtmlTag = ('<' | '</') TagName {TagAttribute} ('/>' | '>')
def htmlTag():
    if found(Token("<")):
        consume(Token("<"))
    else:
        consume(Token("</"))

    tagName()
    
    while found(Token("ident")):
        tagAttribute()

    if found(Token("/>")):
        consume(Token("/>"))
    else:
        consume(Token(">"))


# Cdata = '<![' 'CDATA' '[' {CdataContent} ']]>'
def cdata():
    content = []
    consume(Token("<!["))
    consume(Token("CDATA"))
    consume(Token("["))
    while not found(Token("]]>")):
        content.extend(cdataContent())
    consume(Token("]]>"))
    return content

# TagContent = Cdata | {any token without '<' '</' '>' '&' } 
# Repleces html or xml entitiy references 
# i.e. &amp; => &
def tagContent():
    content = []
    if found(Token("<![")):
        content = cdata() 
    else: 
        while True:
            # if a tagContent is empty
            if found(Token(">")):
                return content 
            if found(Token("</")):
                return content 
            # check if a token is an illegal symbol
            if found(Token("<")) or found(Token(">")) or found(Token("&")):
                error("Illegal symbol: " + token.content)
                
            if found(Token('xmlHtmlEntity')):
                token.content = replaceXmlHtmlEntity(token.content)
            
            content.append(token.content)
            getToken()
            
            # ckeck if a token belongs to rssTag
            if found(Token("<")):
                break
            # check if a token belongs to the ending tag, i.e: '</' TagName '>'
            if found(Token("</")):
                break
       # print "tagContent: ", content
    return content

# XmlTag = '<?' TagName {TagAttribute} '?>'
def xmlTag():
    xmlTagNode = TreeNode()
    consume(Token("<?"))
    xmlTagNode.tagName = tagName()

    while found(Token("ident")):
        xmlTagNode.attributes.append(tagAttribute())

    consume(Token("?>"))

    root.addChild(xmlTagNode)
        
# RssTag = '<' TagName {TagAttribute} ( '/>' | ( '>' {RssTag} TagContent {RssTag} '</' TagName '>' ))
def rssTag():
    rssTagNode = TreeNode()

    # set current rssTag as a child of last opened (and not closed yet) rssTag
    if rssTagStack != []:    
        rssTagStack[-1].children.append(rssTagNode)
    else:
        root.children.append(rssTagNode)

    consume(Token("<"))
    rssTagNode.tagName = tagName()
    while found(Token("ident")):
        rssTagNode.attributes.append(tagAttribute())

    if found(Token("/>")):
        consume(Token("/>"))
        return

    rssTagStack.append(rssTagNode)
    consume(Token(">"))

    if found(Token("<")):
        while found(Token("<")):
            rssTag()
    else:
        rssTagNode.content = tagContent()
    
    if found(Token("<")):
        while found(Token("<")):
            rssTag()

    consume(Token("</"))
    tagName()
    consume(Token(">"))

    check = rssTagStack.pop()
    if check.tagName != rssTagNode.tagName:
        error("There is no ending tag, i.e </example>")

# Body = XmlTag {XmlTag} RssTag {RssTag}
def body():
   while found(Token("<?")):
        xmlTag()

    rssTag()
    while not found(Token(None)):
       rssTag()

# returns:
#   if parsing completed successfully: root of a parsing tree
def program():

    getToken();
    body();
    print "Found nr of errors: ", errorCounter
    if errorCounter == 0:
        print "Parsing comleted successfully!"
        return root
    else:
        print "Parsing error!"
    
    

