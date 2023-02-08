with open('1.html', 'w', encoding='utf-8') as f:
    f.write('<font color="blue">Hello</font> <br>&emsp;<font color="red">World</font>!')

with open('2.html', 'w', encoding='utf-8') as f:
    f.write('<font color="blue">Hello</font>')
    f.write("<br>&emsp;<font color='red'>World</font>!")
    indent = " " * 4
    indent_1 = indent * 2
    f.write(f"<br>{indent_1}<font color='green'>Some</font>!")
    f.write(f"<br>{indent}<font color='yellow'>else</font>!")
    f.write(f"<br>{'&emsp;' * 4}<font color='magenta'>else</font>!")
    f.write(f"{indent}<font color='purple'>andy</font>!")
    li = f"{indent_1}SOMERSBY\n" \
         f"And HERE"
    f.writelines(li)