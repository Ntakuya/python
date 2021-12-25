pantry = [
    ('avocads', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]

for i, (item, count) in enumerate(pantry):
    print('%d: %-10s = %.2f' % (i, item, count))

for i, (item, count) in enumerate(pantry):
    print('%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)))

template = '%s loves food. See %s cook.'
name = 'Max'
formatted = template % (name, name)
print(formatted)

name = 'brad'
formatted = template % (name.title(), name.title())
print(formatted)

key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value}

recordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key}

assert old_way == new_way == recordered

name = 'Max'

tmeplate = '%s loves food. See %s cook.'
before = template % (name, name)

template = '%(name)s loves food. See %(name)s cook.'
after = template % {'name': name}

assert before == after

for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i + 1,
        'item': item.title(),
        'count': round(count)}

    assert before == after

soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)

menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s,'
            'Bu one get two %(oyster)s oysters,'
            'and our special entree is %(special)s.')

formatted = template % menu
print(formatted)

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

formatted = '{1} = {0}'.format(key, value)
print(formatted)

formatted = '{0} loves food. See {0} cook.'.format(name)
print(formatted)

formatted = 'First letter is {menu[oyster]!r}'.format(menu=menu)
print(formatted)
