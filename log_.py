def log(*args):
    print('-------xxxx-------xxxx-------xxxx-------')
    i = 1
    for arg in args:
        print(f"{i * '  '} {arg}")
        i += 1
    print('_______xxxx______xxxx_______xxxx______')
