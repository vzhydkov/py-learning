# -*- coding: utf-8 -*-

"""
# str&bytes in python3
Так как str и bytes не могут быть смешаны, вы всегда должны их явно преобразовывать.
Используйте str.encode(), чтобы перейти от str к bytes и bytes.decode(), чтобы перейти от bytes к str.
Вы также можете использовать bytes(s, encoding=...) и str(b, encoding=...), соответственно.
"""

# strings
"""
The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.
'\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n.
"""

# list comprehension
"""
[ <output value>  for <element> in <list>  <optional criteria> ]
"""