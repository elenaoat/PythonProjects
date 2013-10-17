def main():
    N = 50
    #N = raw_input("Number of cases: ")
    #for rnd in range(1, (N+1)):
        #C = int(raw_input("Credit available: "))
        #I = int(raw_input("Number of items in the store: "))
    with open("large.in", 'r') as f:
        for rnd in range(1, N+1):    
            line = f.readline()    
            C = int(line)
            f.readline()
            products_str = f.readline().split(" ")
            products = [int(product) for product in products_str]
            max_price = max(products)
            rest = C - max_price
            while max_price > C or rest not in products:
                index_max = products.index(max_price)
                products[index_max] = -1
                max_price = max(products)
                rest = C - max_price
            index_max = products.index(max_price)
            if (rest == max_price):
                products[index_max] = None
            index_rest = products.index(rest) + 1
            if (index_max + 1) > index_rest:
                print "Case #{}: {} {}".format(rnd, index_rest, (index_max+1)) 
            else:
                print "Case #{}: {} {}".format(rnd, (index_max+1), index_rest) 

                

if __name__ == '__main__':
    main()
