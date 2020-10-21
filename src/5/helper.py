from urllib.parse import parse_qs


my_values = parse_qs('red=5&blue=0&green=1', keep_blank_values=True)


def get_first_int(values, key, defalut=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    else:
        return 0


green = get_first_int(my_values, 'green')
red = get_first_int(my_values, 'red')
opacity = get_first_int(my_values, 'opacity')


print(green, red, opacity)
