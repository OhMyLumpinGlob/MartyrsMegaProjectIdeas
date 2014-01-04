def pig_latin_translate(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    if string[0] not in consonants:
        return_string = string + 'way'
    else:
        i = 0
        for char in string:
            if char not in consonants:
                return_string = string[i:] + string[:i] + 'ay'
                break
            i += 1
    return return_string

def main():
    while True:
        print "Welcome to Pig Latin Translator!"
        print "\nEnter a word below and it will be translated into Pig Latin:"
        print pig_latin_translate(raw_input())
        print "\nEnter 1 to try again, or 0 to quit:"
        if int(raw_input()):
            pass
        else:
            break
    return

if __name__ == '__main__':
    main()
