#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
import sys
from plex import *

def getUtf8Chars(categories):
    utf8Char = []
    for c in xrange(sys.maxunicode+1):
        u = unichr(c)
        if unicodedata.category(u) in categories:
            print u#, [u.encode("utf-8")], c, unicodedata.name(u)
            utf8Char.append(u.encode("utf-8"))
    return utf8Char


whitespaces = Str(
"\t","\n","\xc2","\x0b","\x0c","\r","\x1c","\x1d","\x1e",
"\x1f"," ","\x85","\xa0","\u1680","\u180e","\u2000","\u2001",
"\u2002","\u2003","\u2004","\u2005","\u2006","\u2007","\u2008",
"\u2009","\u200a","\u2028","\u2029","\u202f","\u205f","\u3000")

currency_symbol = Str(
'$',
 '\xc2\xa2',
 '\xc2\xa3',
 '\xc2\xa4',
 '\xc2\xa5',
 '\xd8\x8b',
 '\xe0\xa7\xb2',
 '\xe0\xa7\xb3',
 '\xe0\xa7\xbb',
 '\xe0\xab\xb1',
 '\xe0\xaf\xb9',
 '\xe0\xb8\xbf',
 '\xe1\x9f\x9b',
 '\xe2\x82\xa0',
 '\xe2\x82\xa1',
 '\xe2\x82\xa2',
 '\xe2\x82\xa3',
 '\xe2\x82\xa4',
 '\xe2\x82\xa5',
 '\xe2\x82\xa6',
 '\xe2\x82\xa7',
 '\xe2\x82\xa8',
 '\xe2\x82\xa9',
 '\xe2\x82\xaa',
 '\xe2\x82\xab',
 '\xe2\x82\xac',
 '\xe2\x82\xad',
 '\xe2\x82\xae',
 '\xe2\x82\xaf',
 '\xe2\x82\xb0',
 '\xe2\x82\xb1',
 '\xe2\x82\xb2',
 '\xe2\x82\xb3',
 '\xe2\x82\xb4',
 '\xe2\x82\xb5',
 '\xe2\x82\xb6',
 '\xe2\x82\xb7',
 '\xe2\x82\xb8',
 '\xea\xa0\xb8',
 '\xef\xb7\xbc',
 '\xef\xb9\xa9',
 '\xef\xbc\x84',
 '\xef\xbf\xa0',
 '\xef\xbf\xa1',
 '\xef\xbf\xa5',
 '\xef\xbf\xa6')

connector_punctuation = Str(
 '_',
 '\xe2\x80\xbf',
 '\xe2\x81\x80',
 '\xe2\x81\x94',
 '\xef\xb8\xb3',
 '\xef\xb8\xb4',
 '\xef\xb9\x8d',
 '\xef\xb9\x8e',
 '\xef\xb9\x8f',
 '\xef\xbc\xbf')

dash_punctuation = Str(
'-',
 '\xd6\x8a',
 '\xd6\xbe',
 '\xe1\x90\x80',
 '\xe1\xa0\x86',
 '\xe2\x80\x90',
 '\xe2\x80\x91',
 '\xe2\x80\x92',
 '\xe2\x80\x93',
 '\xe2\x80\x94',
 '\xe2\x80\x95',
 '\xe2\xb8\x97',
 '\xe2\xb8\x9a',
 '\xe3\x80\x9c',
 '\xe3\x80\xb0',
 '\xe3\x82\xa0',
 '\xef\xb8\xb1',
 '\xef\xb8\xb2',
 '\xef\xb9\x98',
 '\xef\xb9\xa3',
 '\xef\xbc\x8d'

)

open_punctuation = Str (
'(',
 '[',
 '{',
 '\xe0\xbc\xba',
 '\xe0\xbc\xbc',
 '\xe1\x9a\x9b',
 '\xe2\x80\x9a',
 '\xe2\x80\x9e',
 '\xe2\x81\x85',
 '\xe2\x81\xbd',
 '\xe2\x82\x8d',
 '\xe2\x8c\xa9',
 '\xe2\x9d\xa8',
 '\xe2\x9d\xaa',
 '\xe2\x9d\xac',
 '\xe2\x9d\xae',
 '\xe2\x9d\xb0',
 '\xe2\x9d\xb2',
 '\xe2\x9d\xb4',
 '\xe2\x9f\x85',
 '\xe2\x9f\xa6',
 '\xe2\x9f\xa8',
 '\xe2\x9f\xaa',
 '\xe2\x9f\xac',
 '\xe2\x9f\xae',
 '\xe2\xa6\x83',
 '\xe2\xa6\x85',
 '\xe2\xa6\x87',
 '\xe2\xa6\x89',
 '\xe2\xa6\x8b',
 '\xe2\xa6\x8d',
 '\xe2\xa6\x8f',
 '\xe2\xa6\x91',
 '\xe2\xa6\x93',
 '\xe2\xa6\x95',
 '\xe2\xa6\x97',
 '\xe2\xa7\x98',
 '\xe2\xa7\x9a',
 '\xe2\xa7\xbc',
 '\xe2\xb8\xa2',
 '\xe2\xb8\xa4',
 '\xe2\xb8\xa6',
 '\xe2\xb8\xa8',
 '\xe3\x80\x88',
 '\xe3\x80\x8a',
 '\xe3\x80\x8c',
 '\xe3\x80\x8e',
 '\xe3\x80\x90',
 '\xe3\x80\x94',
 '\xe3\x80\x96',
 '\xe3\x80\x98',
 '\xe3\x80\x9a',
 '\xe3\x80\x9d',
 '\xef\xb4\xbe',
 '\xef\xb8\x97',
 '\xef\xb8\xb5',
 '\xef\xb8\xb7',
 '\xef\xb8\xb9',
 '\xef\xb8\xbb',
 '\xef\xb8\xbd',
 '\xef\xb8\xbf',
 '\xef\xb9\x81',
 '\xef\xb9\x83',
 '\xef\xb9\x87',
 '\xef\xb9\x99',
 '\xef\xb9\x9b',
 '\xef\xb9\x9d',
 '\xef\xbc\x88',
 '\xef\xbc\xbb',
 '\xef\xbd\x9b',
 '\xef\xbd\x9f',
 '\xef\xbd\xa2')

initial_punctuation = Str(
'\xc2\xab',
 '\xe2\x80\x98',
 '\xe2\x80\x9b',
 '\xe2\x80\x9c',
 '\xe2\x80\x9f',
 '\xe2\x80\xb9',
 '\xe2\xb8\x82',
 '\xe2\xb8\x84',
 '\xe2\xb8\x89',
 '\xe2\xb8\x8c',
 '\xe2\xb8\x9c',
 '\xe2\xb8\xa0')

final_punctuation = Str(
'\xc2\xbb',
 '\xe2\x80\x99',
 '\xe2\x80\x9d',
 '\xe2\x80\xba',
 '\xe2\xb8\x83',
 '\xe2\xb8\x85',
 '\xe2\xb8\x8a',
 '\xe2\xb8\x8d',
 '\xe2\xb8\x9d',
 '\xe2\xb8\xa1')

close_punctuation = Str(')',
 ']',
 '}',
 '\xe0\xbc\xbb',
 '\xe0\xbc\xbd',
 '\xe1\x9a\x9c',
 '\xe2\x81\x86',
 '\xe2\x81\xbe',
 '\xe2\x82\x8e',
 '\xe2\x8c\xaa',
 '\xe2\x9d\xa9',
 '\xe2\x9d\xab',
 '\xe2\x9d\xad',
 '\xe2\x9d\xaf',
 '\xe2\x9d\xb1',
 '\xe2\x9d\xb3',
 '\xe2\x9d\xb5',
 '\xe2\x9f\x86',
 '\xe2\x9f\xa7',
 '\xe2\x9f\xa9',
 '\xe2\x9f\xab',
 '\xe2\x9f\xad',
 '\xe2\x9f\xaf',
 '\xe2\xa6\x84',
 '\xe2\xa6\x86',
 '\xe2\xa6\x88',
 '\xe2\xa6\x8a',
 '\xe2\xa6\x8c',
 '\xe2\xa6\x8e',
 '\xe2\xa6\x90',
 '\xe2\xa6\x92',
 '\xe2\xa6\x94',
 '\xe2\xa6\x96',
 '\xe2\xa6\x98',
 '\xe2\xa7\x99',
 '\xe2\xa7\x9b',
 '\xe2\xa7\xbd',
 '\xe2\xb8\xa3',
 '\xe2\xb8\xa5',
 '\xe2\xb8\xa7',
 '\xe2\xb8\xa9',
 '\xe3\x80\x89',
 '\xe3\x80\x8b',
 '\xe3\x80\x8d',
 '\xe3\x80\x8f',
 '\xe3\x80\x91',
 '\xe3\x80\x95',
 '\xe3\x80\x97',
 '\xe3\x80\x99',
 '\xe3\x80\x9b',
 '\xe3\x80\x9e',
 '\xe3\x80\x9f',
 '\xef\xb4\xbf',
 '\xef\xb8\x98',
 '\xef\xb8\xb6',
 '\xef\xb8\xb8',
 '\xef\xb8\xba',
 '\xef\xb8\xbc',
 '\xef\xb8\xbe',
 '\xef\xb9\x80',
 '\xef\xb9\x82',
 '\xef\xb9\x84',
 '\xef\xb9\x88',
 '\xef\xb9\x9a',
 '\xef\xb9\x9c',
 '\xef\xb9\x9e',
 '\xef\xbc\x89',
 '\xef\xbc\xbd',
 '\xef\xbd\x9d',
 '\xef\xbd\xa0',
 '\xef\xbd\xa3')

other_punctuation_1 = Str(
'!',
 '"',
 '#',
 '%',
 '&',
 "'",
 '*',
 ',',
 '.',
 '/',
 ':',
 ';',
 '?',
 '@',
 '\\',
 '\xc2\xa1',
 '\xc2\xb7',
 '\xc2\xbf',
 '\xcd\xbe',
 '\xce\x87',
 '\xd5\x9a',
 '\xd5\x9b',
 '\xd5\x9c',
 '\xd5\x9d',
 '\xd5\x9e',
 '\xd5\x9f',
 '\xd6\x89',
 '\xd7\x80',
 '\xd7\x83',
 '\xd7\x86',
 '\xd7\xb3',
 '\xd7\xb4',
 '\xd8\x89',
 '\xd8\x8a',
 '\xd8\x8c',
 '\xd8\x8d',
 '\xd8\x9b',
 '\xd8\x9e',
 '\xd8\x9f',
 '\xd9\xaa',
 '\xd9\xab',
 '\xd9\xac',
 '\xd9\xad',
 '\xdb\x94',
 '\xdc\x80',
 '\xdc\x81',
 '\xdc\x82',
 '\xdc\x83',
 '\xdc\x84',
 '\xdc\x85',
 '\xdc\x86',
 '\xdc\x87',
 '\xdc\x88',
 '\xdc\x89',
 '\xdc\x8a',
 '\xdc\x8b',
 '\xdc\x8c',
 '\xdc\x8d',
 '\xdf\xb7',
 '\xdf\xb8',
 '\xdf\xb9',
 '\xe0\xa0\xb0',
 '\xe0\xa0\xb1',
 '\xe0\xa0\xb2',
 '\xe0\xa0\xb3',
 '\xe0\xa0\xb4',
 '\xe0\xa0\xb5',
 '\xe0\xa0\xb6',
 '\xe0\xa0\xb7',
 '\xe0\xa0\xb8',
 '\xe0\xa0\xb9',
 '\xe0\xa0\xba',
 '\xe0\xa0\xbb',
 '\xe0\xa0\xbc',
 '\xe0\xa0\xbd',
 '\xe0\xa0\xbe',
 '\xe0\xa5\xa4',
 '\xe0\xa5\xa5',
 '\xe0\xa5\xb0',
 '\xe0\xb7\xb4',
 '\xe0\xb9\x8f',
 '\xe0\xb9\x9a',
 '\xe0\xb9\x9b',
 '\xe0\xbc\x84',
 '\xe0\xbc\x85',
 '\xe0\xbc\x86',
 '\xe0\xbc\x87',
 '\xe0\xbc\x88',
 '\xe0\xbc\x89',
 '\xe0\xbc\x8a',
 '\xe0\xbc\x8b',
 '\xe0\xbc\x8c',
 '\xe0\xbc\x8d',
 '\xe0\xbc\x8e',
 '\xe0\xbc\x8f',
 '\xe0\xbc\x90',
 '\xe0\xbc\x91',
 '\xe0\xbc\x92',
 '\xe0\xbe\x85',
 '\xe0\xbf\x90',
 '\xe0\xbf\x91',
 '\xe0\xbf\x92',
 '\xe0\xbf\x93',
 '\xe0\xbf\x94',
 '\xe1\x81\x8a',
 '\xe1\x81\x8b',
 '\xe1\x81\x8c',
 '\xe1\x81\x8d',
 '\xe1\x81\x8e',
 '\xe1\x81\x8f',
 '\xe1\x83\xbb',
 '\xe1\x8d\xa1',
 '\xe1\x8d\xa2',
 '\xe1\x8d\xa3',
 '\xe1\x8d\xa4',
 '\xe1\x8d\xa5',
 '\xe1\x8d\xa6',
 '\xe1\x8d\xa7',
 '\xe1\x8d\xa8',
 '\xe1\x99\xad',
 '\xe1\x99\xae',
 '\xe1\x9b\xab',
 '\xe1\x9b\xac',
 '\xe1\x9b\xad',
 '\xe1\x9c\xb5',
 '\xe1\x9c\xb6',
 '\xe1\x9f\x94',
 '\xe1\x9f\x95',
 '\xe1\x9f\x96',
 '\xe1\x9f\x98',
 '\xe1\x9f\x99',
 '\xe1\x9f\x9a',
 '\xe1\xa0\x80',
 '\xe1\xa0\x81',
 '\xe1\xa0\x82',
 '\xe1\xa0\x83',
 '\xe1\xa0\x84',
 '\xe1\xa0\x85',
 '\xe1\xa0\x87',
 '\xe1\xa0\x88',
 '\xe1\xa0\x89',
 '\xe1\xa0\x8a',
 '\xe1\xa5\x84',
 '\xe1\xa5\x85',
 '\xe1\xa7\x9e',
 '\xe1\xa7\x9f',
 '\xe1\xa8\x9e',
 '\xe1\xa8\x9f',
 '\xe1\xaa\xa0',
 '\xe1\xaa\xa1',
 '\xe1\xaa\xa2',
 '\xe1\xaa\xa3',
 '\xe1\xaa\xa4',
 '\xe1\xaa\xa5',
 '\xe1\xaa\xa6',
 '\xe1\xaa\xa8',
 '\xe1\xaa\xa9',
 '\xe1\xaa\xaa',
 '\xe1\xaa\xab',
 '\xe1\xaa\xac',
 '\xe1\xaa\xad',
 '\xe1\xad\x9a',
 '\xe1\xad\x9b',
 '\xe1\xad\x9c',
 '\xe1\xad\x9d',
 '\xe1\xad\x9e',
 '\xe1\xad\x9f',
 '\xe1\xad\xa0',
 '\xe1\xb0\xbb',
 '\xe1\xb0\xbc',
 '\xe1\xb0\xbd',
 '\xe1\xb0\xbe',
 '\xe1\xb0\xbf',
 '\xe1\xb1\xbe',
 '\xe1\xb1\xbf',
 '\xe1\xb3\x93',
 '\xe2\x80\x96',
 '\xe2\x80\x97',
 '\xe2\x80\xa0',
 '\xe2\x80\xa1',
 '\xe2\x80\xa2',
 '\xe2\x80\xa3',
 '\xe2\x80\xa4',
 '\xe2\x80\xa5',
 '\xe2\x80\xa6',
 '\xe2\x80\xa7',
 '\xe2\x80\xb0',
 '\xe2\x80\xb1',
 '\xe2\x80\xb2',
 '\xe2\x80\xb3',
 '\xe2\x80\xb4',
 '\xe2\x80\xb5',
 '\xe2\x80\xb6',
 '\xe2\x80\xb7',
 '\xe2\x80\xb8',
 '\xe2\x80\xbb',
 '\xe2\x80\xbc',
 '\xe2\x80\xbd',
 '\xe2\x80\xbe',
 '\xe2\x81\x81',
 '\xe2\x81\x82',
 '\xe2\x81\x83',
 '\xe2\x81\x87',
 '\xe2\x81\x88',
 '\xe2\x81\x89',
 '\xe2\x81\x8a',
 '\xe2\x81\x8b',
 '\xe2\x81\x8c',
 '\xe2\x81\x8d',
 '\xe2\x81\x8e',
 '\xe2\x81\x8f',
 '\xe2\x81\x90',
 '\xe2\x81\x91',
 '\xe2\x81\x93',
 '\xe2\x81\x95',
 '\xe2\x81\x96',
 '\xe2\x81\x97',
 '\xe2\x81\x98',
 '\xe2\x81\x99',
 '\xe2\x81\x9a',
 '\xe2\x81\x9b',
 '\xe2\x81\x9c',
 '\xe2\x81\x9d',
 '\xe2\x81\x9e',
 '\xe2\xb3\xb9',
 '\xe2\xb3\xba',
 '\xe2\xb3\xbb',
 '\xe2\xb3\xbc',
 '\xe2\xb3\xbe',
 '\xe2\xb3\xbf',
 '\xe2\xb8\x80',
 '\xe2\xb8\x81',
 '\xe2\xb8\x86',
 '\xe2\xb8\x87',
 '\xe2\xb8\x88',
 '\xe2\xb8\x8b',
 '\xe2\xb8\x8e',
 '\xe2\xb8\x8f',
 '\xe2\xb8\x90',
 '\xe2\xb8\x91',
 '\xe2\xb8\x92',
 '\xe2\xb8\x93',
 '\xe2\xb8\x94',
 '\xe2\xb8\x95',
 '\xe2\xb8\x96',
 '\xe2\xb8\x98',
 '\xe2\xb8\x99',
 '\xe2\xb8\x9b',
 '\xe2\xb8\x9e',
 '\xe2\xb8\x9f',
 '\xe2\xb8\xaa',
 '\xe2\xb8\xab',
 '\xe2\xb8\xac',
 '\xe2\xb8\xad',
 '\xe2\xb8\xae')

other_punctuation_2 = Str(
 '\xe2\xb8\xb0',
 '\xe2\xb8\xb1',
 '\xe3\x80\x81',
 '\xe3\x80\x82',
 '\xe3\x80\x83',
 '\xe3\x80\xbd',
 '\xe3\x83\xbb',
 '\xea\x93\xbe',
 '\xea\x93\xbf',
 '\xea\x98\x8d',
 '\xea\x98\x8e',
 '\xea\x98\x8f',
 '\xea\x99\xb3',
 '\xea\x99\xbe',
 '\xea\x9b\xb2',
 '\xea\x9b\xb3',
 '\xea\x9b\xb4',
 '\xea\x9b\xb5',
 '\xea\x9b\xb6',
 '\xea\x9b\xb7',
 '\xea\xa1\xb4',
 '\xea\xa1\xb5',
 '\xea\xa1\xb6',
 '\xea\xa1\xb7',
 '\xea\xa3\x8e',
 '\xea\xa3\x8f',
 '\xea\xa3\xb8',
 '\xea\xa3\xb9',
 '\xea\xa3\xba',
 '\xea\xa4\xae',
 '\xea\xa4\xaf',
 '\xea\xa5\x9f',
 '\xea\xa7\x81',
 '\xea\xa7\x82',
 '\xea\xa7\x83',
 '\xea\xa7\x84',
 '\xea\xa7\x85',
 '\xea\xa7\x86',
 '\xea\xa7\x87',
 '\xea\xa7\x88',
 '\xea\xa7\x89',
 '\xea\xa7\x8a',
 '\xea\xa7\x8b',
 '\xea\xa7\x8c',
 '\xea\xa7\x8d',
 '\xea\xa7\x9e',
 '\xea\xa7\x9f',
 '\xea\xa9\x9c',
 '\xea\xa9\x9d',
 '\xea\xa9\x9e',
 '\xea\xa9\x9f',
 '\xea\xab\x9e',
 '\xea\xab\x9f',
 '\xea\xaf\xab',
 '\xef\xb8\x90',
 '\xef\xb8\x91',
 '\xef\xb8\x92',
 '\xef\xb8\x93',
 '\xef\xb8\x94',
 '\xef\xb8\x95',
 '\xef\xb8\x96',
 '\xef\xb8\x99',
 '\xef\xb8\xb0',
 '\xef\xb9\x85',
 '\xef\xb9\x86',
 '\xef\xb9\x89',
 '\xef\xb9\x8a',
 '\xef\xb9\x8b',
 '\xef\xb9\x8c',
 '\xef\xb9\x90',
 '\xef\xb9\x91',
 '\xef\xb9\x92',
 '\xef\xb9\x94',
 '\xef\xb9\x95',
 '\xef\xb9\x96',
 '\xef\xb9\x97',
 '\xef\xb9\x9f',
 '\xef\xb9\xa0',
 '\xef\xb9\xa1',
 '\xef\xb9\xa8',
 '\xef\xb9\xaa',
 '\xef\xb9\xab',
 '\xef\xbc\x81',
 '\xef\xbc\x82',
 '\xef\xbc\x83',
 '\xef\xbc\x85',
 '\xef\xbc\x86',
 '\xef\xbc\x87',
 '\xef\xbc\x8a',
 '\xef\xbc\x8c',
 '\xef\xbc\x8e',
 '\xef\xbc\x8f',
 '\xef\xbc\x9a',
 '\xef\xbc\x9b',
 '\xef\xbc\x9f',
 '\xef\xbc\xa0',
 '\xef\xbc\xbc',
 '\xef\xbd\xa1',
 '\xef\xbd\xa4',
 '\xef\xbd\xa5',
 '\xf0\x90\x84\x80',
 '\xf0\x90\x84\x81',
 '\xf0\x90\x8e\x9f',
 '\xf0\x90\x8f\x90',
 '\xf0\x90\xa1\x97',
 '\xf0\x90\xa4\x9f',
 '\xf0\x90\xa4\xbf',
 '\xf0\x90\xa9\x90',
 '\xf0\x90\xa9\x91',
 '\xf0\x90\xa9\x92',
 '\xf0\x90\xa9\x93',
 '\xf0\x90\xa9\x94',
 '\xf0\x90\xa9\x95',
 '\xf0\x90\xa9\x96',
 '\xf0\x90\xa9\x97',
 '\xf0\x90\xa9\x98',
 '\xf0\x90\xa9\xbf',
 '\xf0\x90\xac\xb9',
 '\xf0\x90\xac\xba',
 '\xf0\x90\xac\xbb',
 '\xf0\x90\xac\xbc',
 '\xf0\x90\xac\xbd',
 '\xf0\x90\xac\xbe',
 '\xf0\x90\xac\xbf',
 '\xf0\x91\x82\xbb',
 '\xf0\x91\x82\xbc',
 '\xf0\x91\x82\xbe',
 '\xf0\x91\x82\xbf',
 '\xf0\x91\x83\x80',
 '\xf0\x91\x83\x81',
 '\xf0\x92\x91\xb0',
 '\xf0\x92\x91\xb1',
 '\xf0\x92\x91\xb2',
 '\xf0\x92\x91\xb3')
