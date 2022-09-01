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
    
    pattern = r'( +)- (.*)\n'
    replacement = r'<ul><li><ul><li>\2</li></ul></li></ul>'
    html = re.sub(pattern, replacement, html)
    
    pattern = r'- (.*)\n'
    replacement = r'<ul><li>\1</li></ul>'
    html = re.sub(pattern, replacement, html)
    
#     <li>Tea
#     <ul>
#       <li>Black tea</li>
#       <li>Green tea</li>
#     </ul>
#   </li>

# <li>Tea</li></ul>
#     <ul>
#       <li>Black tea</li>
#       <li>Green tea</li>
#     </ul>
#   </li>
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
