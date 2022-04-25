#!/usr/bin/env python3
# Добавляет маркеры Википедии в начало каждой стороки тескта
# сохраняемого в буфере обмена

import pyperclip

text = pyperclip.paste()

#  разделить строки и добавить звездочки
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
