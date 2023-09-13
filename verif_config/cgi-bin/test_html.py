from lxml import etree

htmlUl = etree.XML('<ul/>')
li1 = etree.XML("<li/>")
li2 = etree.XML("<li/>")
span1 = etree.XML('<span/>')
span2 = etree.XML('<span/>')
sel1 = etree.XML('<select/>')
sel2 = etree.XML('<select/>')
opt1 = etree.XML('<option/>')
opt2 = etree.XML('<option/>')

htmlUl.append(li1)
li1.append(span1)
li1.append(sel1)
sel1.append(opt1)

htmlUl.append(li2)
li2.append(span2)
li2.append(sel2)
sel2.append(opt2)

htmlUl.set('id', 'first-ul')

span1.text = 'CONFIG_1'
span1.set('class', 'caret')
sel1.set('id', 'CONFIG_1')
sel1.set('class', 'set')
opt1.set('value', '123')
opt1.set('selected', '')
opt1.text = 'abc'

span2.text = 'CONFIG_2'
span2.set('class', 'caret')
sel2.set('id', 'CONFIG_2')
sel2.set('class', 'set')
opt2.set('value', '223')
opt2.text = 'abc'

html_str2 = etree.tostring(htmlUl, pretty_print=True, encoding="utf-8")

print(html_str2.decode('utf-8'))
