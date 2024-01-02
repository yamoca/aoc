file = open("input.txt", "r")

digit_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

mapping = {}

def insert_nums(line):
    for key in mapping: 
        if mapping[key] != -1:
            line = line[:mapping[key]] + str(digit_dict[key]) + line[mapping[key]:]
            for key in mapping: 
                if mapping[key] != -1:
                    mapping[key] += 1
    
    print(line)


def populate_mapping(line):
    for key in digit_dict:
        mapping[key] = line.find(key)

    insert_nums(line)    


   

for line in file:
    populate_mapping(line)








file.close()