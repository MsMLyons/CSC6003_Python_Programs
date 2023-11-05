string = 'abc'

print(string.encode('greek8'))
print(string.encode('x_mac_korean'))
print(string.encode('maccyrillic'))

txt = 'Hi there!'
x = txt.encode()
print(x)