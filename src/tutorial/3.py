# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

print(2 + 2)

print(50 - 5*6)

print((50 - 5*6) / 4)

print(
    8 / 5  # division always returns a floating point number
)

print( 17 / 3 )

print( 17 // 3 )

print( 17 % 3 )

print( 5 * 3 + 2 )

def calc_area(width, height):
    print(width * height)

calc_area(width=20,height = 5 * 9)

def undefined_variables():
    try:
        n
    except NameError as error:
        print(error)

undefined_variables()

print(4 * 3.75 - 1)

def cal_amount(price, tax):
    print(price * tax)

cal_amount(price=100.50, tax=12.5 / 100)