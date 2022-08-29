import re

def markdown(markdown):
    pattern = r'\*\*(.*?)\*\*'
    replacement = r'<b>\1</b>'
    html = re.sub(pattern, replacement, markdown)

    pattern = r'\*(.*?)\*'
    replacement = r'<i>\1</i>'
    html = re.sub(pattern, replacement, html)

    # markdown = "[I'm an inline-style link](https://www.google.com)";
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html);

    pattern = r'\### (.*)'
    replacement = r'<h3>\1</h3>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\## (.*)'
    replacement = r'<h2>\1</h2>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\# (.*)'
    replacement = r'<h1>\1</h1>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'- (.*)\n'
    replacement = r'<ul><li>\1</li></ul>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'\n'
    replacement = r'<br>'
    html = re.sub(pattern, replacement, html)
    
    # phoneNumRegex = re.compile(pattern)
    # mo = phoneNumRegex.search(html)
    # print(mo.groups())
    return html
