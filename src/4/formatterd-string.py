key = 'my_var'
value = 1.234
pantry = [
    ('avocads', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

f_string = f'{key:<10} = {value:.2f}'
c_tuple = '%-10s = %.2f' % (key, value)
str_args = '{:<10} = {:.2f}'.format(key, value)
str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))

    f_string = f'#{i + 1}: {item.title():<10s} = {round(count)}'

    assert old_style == new_style == f_string

for i, (item, count) in enumerate(pantry):
    print(f'#{ i + 1 }:'
          f'{item.title():<10s} = '
          f'{round(count)}')
