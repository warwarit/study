#!/usr/bin/env python3
# Добавляет маркеры Википедии в начало каждой стороки тескта
# сохраняемого в буфере обмена

import pyperclip

text = pyperclip.paste()

# TODO: разделить строки и добавить звездочки

pyperclip.copy(text)
