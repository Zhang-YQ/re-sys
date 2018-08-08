html_strings="aaatest"

with open('../home/wwwroot1/index.html', 'w') as file_operate:
    file_operate.write(html_strings)
with open('../home/wwwroot1/index.html','r') as f:
    print(f.read())

