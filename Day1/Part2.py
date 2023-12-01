import regex as re

with open('input1.txt') as f:
    calibs=f.read().splitlines()

digit_dict = {
    #'zero': 0,
    'one': "o1ne",
    'two': "t2wo",
    'three': "t3hree",
    'four': "f4our",
    'five': "f5ive",
    'six': "s6ix",
    'seven': "s7even",
    'eight': "e8ight",
    'nine': "n9ine"
}

calsum=0
for calib in calibs:
    spelled_digits=(re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine)',calib,overlapped=True))
    for dig in spelled_digits:
        calib=calib.replace(dig,str(digit_dict[dig]))
    print(calib)
    rcalib=calib[::-1]
    calsum+=int(re.search(r"\d",calib).group()+re.search(r"\d",rcalib).group())
print(calsum)
