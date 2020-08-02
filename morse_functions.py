char_to_dots = {
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
        try:
            for number, value in enumerate(message_split):
                if value in char_to_dots:
                    message_split[number] = char_to_dots[value]
                if value not in char_to_dots:
                    message_split[number] = "#"
        except KeyError:
            pass
        else:
            return ' '.join(message_split)

    def decode_morse(self, message):
        split_message = message.split()
        inverted_char = {v: k for k, v in char_to_dots.items()}
        try:
            for number, value in enumerate(split_message):
                if value in inverted_char:
                    split_message[number] = inverted_char[value]
                if value not in inverted_char:
                    split_message[number] = "#"
        except KeyError:
            pass
        else:
            return "".join(split_message)
