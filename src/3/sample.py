a = b'h\x65llo'

# Bytes
print(list(a))
print(a)

# Unicodeも利用可能
a = 'a\u0300 props'
print(list(a))
print(a)
