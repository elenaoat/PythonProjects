def count(start, step=1):
    while True:
        yield start
        start += step

def cycle(iterable):
    while True:
        iterb = iterable
        for letter in iterb:
            yield letter        

def repeat(obj, times=None):
    if times:
        for time in xrange(times):
            yield obj
            times -= 1
    elif times is None:         
        while True:
            yield obj
def chain(*iterables):
    for iterable in iterables:
        for elem in iterable:
            yield elem
def 
#count_test = count(-10, -2)
#cycle_test = cycle([1, 2])
#repeat_test = repeat(5)
#chain_test = chain("ABC", "DEF")
chain_test = chain([1, 2, 3], [4, 5, 6])
for i in range(6):
    print chain_test.next()
#    print count_test.next()
#    print cycle_test.next()
#    print repeat_test.next()

