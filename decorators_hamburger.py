def bread_and_veggies(func):
    def inner(cheese_slices):
        print "rye bread"
        print "lettuce"
        print "tomatoes"
        print "no mayo, no ketchup!! it's unhealthy!"
        func(cheese_slices)
        print "bread"
    return inner

def make_it_cheeeesy(func):
    def inner(cheese_slices):
        if cheese_slices > 0:
            print "cheese"
            func(cheese_slices)
            for cheese_slice in range(cheese_slices-1):
                print "cheese"
        else:
            func(cheese_slices)
    return inner

@bread_and_veggies
@make_it_cheeeesy
def beef(cheese_slices):
    print "beef"
@bread_and_veggies
@make_it_cheeeesy
def chicken(cheese_slices):
    print "chicken"


def main():
    # first let's make a beef hamburger
    print "A yummy beef hamburger contents:"
    beef(2)
    # I would also have a chicken one, please
    print "And a chicken one's:"
    chicken(1)

if __name__ == "__main__":
    main()
