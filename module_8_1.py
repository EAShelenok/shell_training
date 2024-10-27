def add_everything_up(a, b):
    print(f"Let's try to sum up {a} and {b}...")
    try:
        c = a + b
        return str(f'Success!!! Result: {c}')
    except TypeError as exc:
        print(f'We have a problem ({exc}). But there is a way out =)')
        c = str(a) +  str(b)
        return str(f'Alternative result: {c}')

if __name__ == '__main__':
    print(add_everything_up(13.5, 10))
    print(add_everything_up('Apple', 3.5))
    print(add_everything_up(100, 'Watermelon'))
    print(add_everything_up('Blueberry', 'Pineapple'))
