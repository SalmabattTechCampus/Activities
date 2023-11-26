

def is_vowel(letter):
    if letter in 'aeiouAEIOU':
        return True
    else:
        return False

def main():
    count = 0
    string = input('Enter a text: ')
    for ch in string:
        if(is_vowel(ch)):
            count += 1

    print('Number of vowels are', count)

main()
Output