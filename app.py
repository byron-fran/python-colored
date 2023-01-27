from colored import fg, bg, attr;

word = fg(1)  + bg(10) # background is green
print(word + 'hola mundo' + attr(0))