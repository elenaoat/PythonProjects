
def main():
    mapping = {"a": "2", "b": "22", "c": "222",
            "d": "3", "e": "33", "f": "333", 
            "g": "4", "h": "44", "i": "444",
            "j": "5", "k": "55", "l": "555",
            "m": "6", "n": "66", "o": "666",
            "p": "7", "q": "77", "r": "777",
            "s": "7777", "t": "8", "u": "88",
            "v": "888", "w": "9", "x": "99",
            "y": "999", "z": "9999", " ": "0"}

    with open("C-large-practice.in") as f:
        for rnd, line in enumerate(f):
            line = line.rstrip("\n")
            letters = list(line) 
            numbers = [mapping[letter] for letter in letters]
            numbers_w_spaces = [numbers[0]]
            
            for index, num in enumerate(numbers[1:]):
                prev_num = numbers[index]
                #print index, num, prev_num 
                if num[0] == prev_num[0]:
                    numbers_w_spaces.extend([" ", num])
                else:
                    numbers_w_spaces.append(num)
            print "Case #{}: {}".format(str(rnd+1), ''.join(numbers_w_spaces)) 




if __name__ == "__main__":
    main()
