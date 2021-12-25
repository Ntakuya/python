from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=1', keep_blank_values=True)

print(repr(my_values))

print('RED', my_values.get('red'))
print('Green', my_values.get('green'))
print('Opacity', my_values.get('Opacity'))

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print(my_values.get('opacity'))
print(my_values.get('opacity', ['']))
print(my_values.get('opacity', [''])[0])

print(f'Red: {red!r}')
print(f'Green: {green!r}')
print(f'Opacity: {opacity!r}')

red = int(my_values.get('red', [''])[0] or 0)

print(f'Red; {red!r}')

red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0

print(repr(red))

green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

print(green)
