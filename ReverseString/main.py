def reverse_string(string):
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.reverse()
    return_string = ''
    for char in char_list:
        return_string += char
    return return_string

def main():
    while True:
        print "Welcome to Reverse String! Want to reverse a string? Well, then, you're in luck!"
        print "Enter your string below and wait for your results"
        print "The result is: " + reverse_string(raw_input())
        if int(raw_input("1 to try again, 0 to quit\n")):
            pass
        else:
            break
    return

if __name__ == '__main__':
    main()
