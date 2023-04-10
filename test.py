def foo():
    if not hasattr(foo, 'counter'):
        foo.counter = 0
    foo.counter +=1
    print(foo.counter)
    return None

print(foo())
print(foo())
print(foo())

