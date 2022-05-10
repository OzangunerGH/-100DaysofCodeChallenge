morse_code = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

def morse_translator():
    user_string = input('Input any string to convert to Morse Alphabet\n').lower()
    while user_string != 'exit':
        morse_string = ""
        for letter in user_string:
            try:
                test = morse_code[letter]
            except KeyError:
                print('Wrong String Input. A string can only contain numbers, letters and spaces.\n')
                morse_translator()
            morse_string += morse_code[letter] + " "
        print(f'Morse output of {user_string} is:  {morse_string}\n')
        user_string = input('Input any string to convert to Morse Alphabet\n').lower()

morse_translator()

