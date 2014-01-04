def is_palindrome(string):
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.reverse()
    reverse_string = ''
    for entry in char_list:
        reverse_string += entry
    return string == reverse_string

def main():
    while True:
        print "Welcome to Palindrome Checker!"
        print "Want to check if a word is a palindrome? Enter it below and find out!"
        print "\nEnter the word you want to check:"
        string = raw_input()
        if is_palindrome(string):
            print "Yes! " + string + " is a palindrome!"
        else:
            print "No! " + string + " is not a palindrome!"
        print "\nEnter 1 to try again, 0 to quit:"
        if int(raw_input()):
            pass
        else:
            break
    return

if __name__ == '__main__':
    main()
