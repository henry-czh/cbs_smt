#!/bin/env python
from lxml import etree

def GetSvg(svgfile):
    parser = etree.HTMLParser(encoding='utf-8')
    svg = etree.parse(svgfile,parser=parser)

    return etree.tostring(svg,encoding='utf-8',pretty_print=True,method='html')