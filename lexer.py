#!/usr/bin/python
# -*- coding: utf-8 -*-

from plex import *
import patterns 
from token import Token
import string


letter = Range("AZaz") | Str("ą", "ć", "ę", "ł","ń","ó",
        "ś","ż","ź","Ą","Ć","Ę","Ł","Ń","Ó","Ś","Ż","Ź")
identCharacter = Str("_", "-", ".")
digit = Range("09")

# Tokens:
identifier = letter + Rep(letter | digit | identCharacter)
number = Rep1(digit)
comment = Str("<!--") + Rep(AnyChar) + Str("-->")
symbol = Str("</", "/>", "<?", "?>", "<![", "]]>", '="')
hexadecimal = Rep1(digit | Range('AFaf'))
keyword = Str("CDATA")

# Character reference or named entity, i.e. &#xc2;, &nbsp;, &gt;
# Possible formats:
# &#nnnn, &#xhhhh, &name
# where: n - code point in decimal form
#        h - code point in hexadecimal form 
#        name - name of entity
numericCharRef = ((Str('&#') + Rep1(digit)) + Str(';') | 
                 (Str('&#x') + Seq(hexadecimal, hexadecimal, hexadecimal, hexadecimal)) + Str(';') |
                 (Str('&') + identifier + Str(';')))


# otherSymbol is any char, which is not an an indentifier, a keyword,
# a symbol, a number, a whitespace or a comment
otherSymbol = AnyChar

class Lexer(Scanner):

    lexicon = Lexicon([
    	(keyword,	TEXT),
        (patterns.close_punctuation, TEXT),
        (patterns.open_punctuation, TEXT),
        (patterns.connector_punctuation, TEXT),
        (patterns.dash_punctuation, TEXT),
        (patterns.currency_symbol, TEXT),
        (patterns.initial_punctuation, TEXT),
        (patterns.final_punctuation, TEXT),
        (patterns.other_punctuation_1, TEXT),
        (patterns.other_punctuation_2, TEXT),
        (numericCharRef, 'xmlHtmlEntity'),
        (identifier,'ident'),
        (number,    'number'),
        (patterns.whitespaces, IGNORE),
        (comment,   IGNORE),
        (symbol, 	TEXT),
        (otherSymbol,    TEXT)
        ])
    def __init__(self, stream):
        Scanner.__init__(self, self.lexicon, stream)


def initialize(stream):
	global lexer
	lexer = Lexer(stream)

def read():
    temp = lexer.read()
    token = Token(temp[0])
    token.content = temp[1]
    return token

def read2():
    return lexer.read()

def position():
	return lexer.position()
