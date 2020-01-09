import re
text_obj = open('./eth1to15.txt', encoding='gb18030')
file_content = text_obj.read()
pattern = re.compile(r'''href="/detail/....''')
result = pattern.findall(file_content)
