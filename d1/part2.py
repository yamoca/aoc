file = open("input.txt", "r")
sum = 0 
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

def calccalval(word):
    nums = ""
    for letter in word:
        if letter.isnumeric():
            nums += letter
    
    ans = nums[0] + nums[len(nums)-1]
    return int(ans)


def insert_nums(line):
    global sum
    for key in mapping: 
        if mapping[key] != -1:
            line = line[:mapping[key]] + str(digit_dict[key]) + line[mapping[key]:]
            for key in mapping: 
                if mapping[key] != -1:
                    mapping[key] += 1
    
    sum += calccalval(line) 


def populate_mapping(line):
    for key in digit_dict:
        mapping[key] = line.find(key)

    insert_nums(line)    


   

for line in file:
    populate_mapping(line)



print(sum)




file.close()