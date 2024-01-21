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
recursion = 0

def calccalval(word):
    nums = ""
    for letter in word:
        if letter.isnumeric():
            nums += letter
    
    ans = nums[0] + nums[-1]
    return int(ans)


def insert_nums(line, recursionlimit, current_count=0):
    global sum
    for key in mapping: 
        if mapping[key][0] != -1: # mapping[key] is a list that could be empty
            line = line[:mapping[key][0]+1] + str(digit_dict[key]) + line[mapping[key][0]+1:]
            for key in mapping: # because a new digit has been inserted, the length of the string has changed and so indexs need to shift positions
                if mapping[key][0] != -1:
                    mapping[key][0] += 1

    if current_count >= recursionlimit:
        #print(mapping)
        print(line)
        #print(calccalval(line))
        sum += calccalval(line) 
        #print(sum)
        #print(mapping)
        return

    populate_mapping(line, current_count + 1) # recursive

def populate_mapping(line, limit, current_count=0):
    for key in digit_dict:
        list = [] 
        list.append(line.find(key))
        mapping[key] = list
       

    print(mapping)
    insert_nums(line, 4, current_count + 1)    

       



# clumsy but could use recursion method ie insert numbers and map multiple times: iteration 1: "sevenseven" -> "s7evenseven" iteration 2: "s7evenseven" -> "s7evens7even" 

populate_mapping("1234fourjdfoursevenfivesixnine", 3)
##for line in file:
    ##populate_mapping(line)


print(recursion)

#print(sum)


# NOT WORKING BECAUSE OF MULTIPLE NUMBERS IN WORD E.G "1234sevenaljdfourseven" should be 17 but the inserter only detects one number word per line so only converts first 7 

file.close()