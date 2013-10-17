"""Calculate minimum scalar product.
"""


def main():
    N = 1000
    with open("vectors") as f, open("vector_result", "a") as f_:
        for rnd in range(N):
#            print "-----------------"
            dim = int(f.readline())
            vect_a = [int(elem) for elem in f.readline().split()]
           # print "vector a:", vect_a
            vect_b = [int(elem) for elem in f.readline().split()]
           # print "vector b:", vect_b
            maxs = []
            mins = []
            
            k = 2
            if len(vect_a) < 2:
                k = 1
            for num in range(k):
                if max(vect_a) >= max(vect_b):
                    max_a = max(vect_a)                    
                    maxs.append(max_a)    
                    vect_a.remove(max_a)
                    min_b = min(vect_b)
                    vect_b.remove(min_b)
                    mins.append(min_b)
                else:
                    max_b = max(vect_b)
                    maxs.append(max_b)
                    vect_b.remove(max_b)
                    min_a = min(vect_a)
                    vect_a.remove(min_a)
                    mins.append(min_a)
           # print maxs, mins
           #print vect_a, vect_b
            
            if k == 1:
                scalar_product = maxs[0]*mins[0]
                if maxs[0] < 0 and mins[0] < 0:
                    print "both negative"
            else:
                scalar_product = maxs[0]*mins[0] + maxs[1]*mins[1]
                if (maxs[0] < 0 and mins[0] < 0) or (maxs[1] < 0 and mins[1]):
                    print "both negative"
                for i in range(dim-2):
                    scalar_product = scalar_product + vect_a[i]*vect_b[i]
            f_.write("Case #{}: {}\n".format(rnd+1, scalar_product))
            scalar_product = 0 

if __name__ == '__main__':
    main()
