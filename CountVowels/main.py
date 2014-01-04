def count_vowels(string):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char not in vowels:
            pass
        else:
            if char in 'aA':
                a += 1
            elif char in 'eE':
                e += 1
            elif char in 'iI':
                i += 1
            elif char in 'oO':
                o += 1
            elif char in 'uU':
                u += 1
    return 'Total Vowels: ' + str(a+e+i+o+u) + '\nNumber of As: ' + str(a) + '\nNumber of Es: ' + str(e) + '\nNumber of Is: ' + str(i) + '\nNumber of Os: ' + str(o) + '\nNumber of Us: ' + str(u)

def main():
    while True:
        print "Welcome to Vowel Counter!"
        print "Want to know how many vowels are in a word, or any other chunk of text? Then enter it now!"
        print "\nPlease enter the text to be analysed below:"
        print count_vowels(raw_input())
        print "Enter 1 to try again, 0 to quit:"
        if int(raw_input()):
            pass
        else:
            break
    return

if __name__ == '__main__':
    main()
