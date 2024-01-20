# chat gpt is shit

def word_to_number(word):
    word_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }

    # Convert the word to its numeric value
    result = 0
    current_number = 0

    for w in word.split():
        if w in word_dict:
            current_number += word_dict[w]
        elif w == 'and':
            continue
        else:
            current_number *= word_dict.get(w, 1)

    result += current_number

    return result

def extract_numbers(input_string):
    result = ''.join(char if char.isdigit() else str(word_to_number(char)) for char in input_string.split())
    return result

# Example usage:
input_str = "1234seven"
output_str = extract_numbers(input_str)
print(output_str)
