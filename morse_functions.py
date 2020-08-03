morse_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }


class MorseFunctions:
    def encode_morse(self, message):
        message_split = [_ for _ in message.upper()]
        while " " in message_split:
            message_split.remove(" ")
#       Had a problem with filtering whitespaces here, I eventually found another way (Hope it's pythonic enough):
#         message_split = [_ for _ in message_split if _]
#         print(message_split)
        try:
            for number, value in enumerate(message_split):
                if value in morse_codes:
                    message_split[number] = morse_codes[value]
                if value not in morse_codes:
                    message_split[number] = "#"
        except KeyError:
            pass
        else:
            return ' '.join(message_split)

    def decode_morse(self, message):
        message_split = message.split(" ")
        message_split = [_ for _ in message_split if _]
        inverted_char = {v: k for k, v in morse_codes.items()}
        try:
            for number, value in enumerate(message_split):
                if value in inverted_char:
                    message_split[number] = inverted_char[value]
                if value not in inverted_char:
                    message_split[number] = "#"
        except KeyError:
            pass
        else:
            return "".join(message_split)
