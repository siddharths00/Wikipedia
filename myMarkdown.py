"""
Markdown Function
=================
This is the Markdown parser which takes in input as string and returns the 
HTML text to be given to Markdown parser.

"""

import re

def markdown(markdown):
    """
    This takes as parameters

    :Input:
          :markdown: markdown text to be parsed
    :Returns:
          :the html text
    """
    pattern = r'\*\*(.*?)\*\*'
    replacement = r'<b>\1</b>'
    html = re.sub(pattern, replacement, markdown)

    pattern = r'\*(.*?)\*'
    replacement = r'<i>\1</i>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    replacement = r'<a href="\2">\1</a>'
    html = re.sub(pattern, replacement, html);

    pattern = r'\### (.*)'
    replacement = r'<h3>\1</h3>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\## (.*)'
    replacement = r'<h2>\1</h2>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\# (.*)'
    replacement = r'<h1>\1</h1>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'( +)- (.*)\n'
    replacement = r'<ul><li><ul><li>\2</li></ul></li></ul>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'- (.*)\n'
    replacement = r'<ul><li>\1</li></ul>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'</li></ul><ul><li><ul><li>'
    replacement = r'<ul><li>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'</li></ul><ul><li>'
    replacement = r'</li><li>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\n'
    replacement = r'<br>'
    html = re.sub(pattern, replacement, html)
    return html
