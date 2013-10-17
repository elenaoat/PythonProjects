
def main():
    with open("file.txt") as f:
        for rnd, line in enumerate(f):
            line = line.rstrip()
            words = line.split(" ")
            words_reversed = [word for word in reversed(words)]
            line_reversed = " ".join(words_reversed) 
            print "Case #{}: {}".format(rnd+1, line_reversed)



if __name__ == '__main__':
    main()
