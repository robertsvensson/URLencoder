from URLencode import URLencode

unicodeString = '<h1>'

enc = URLencode()

print enc.encodeString(unicodeString)
