def readinput(file):
    sum = 0
    for line in file:
        sum += calccalval(line)

    return sum



def calccalval(word):
    nums = ""
    for letter in word:
        if letter.isnumeric():
            nums += letter
    
    nums += isdigit(word)

    ans = nums[0] + nums[len(nums)-1]
    return int(ans)

print(readinput(open("input.txt", "r")))
