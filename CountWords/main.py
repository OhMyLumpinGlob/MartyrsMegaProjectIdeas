def get_count(string):
    count_dict = {}
    new_string = ''
    string = string.lower()
    for char in string:
        if char in 'abcdefghijklmnopqrstuvwxyz ':
            new_string += char
    word_list = new_string.split()
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return (len(word_list),count_dict)

def main():
    while True:
        print "Welcome to Word Counter!"
        print "Want to know how many words are in a chunk of text? Enter it below and find out!"
        string = raw_input("Enter the text below:\n")
        results = get_count(string)
        print "There were " + str(results[0]) + " words total."
        print "The following is a breakdown of the word frequency:"
        for entry in results[1]:
            print str(entry) + ": " + str(results[1][entry])
        if int(raw_input("\nEnter 1 to try again, 0 to quit:\n")):
            pass
        else:
            break
    return

if __name__ == '__main__':
    main()
