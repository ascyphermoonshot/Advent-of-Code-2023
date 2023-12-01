import regex as re

 with open('/storage/emulated/0/Download/input1.txt') as f:
     calibs=f.read().splitlines()

 digit_dict = {
     #'zero': 0,
     'one': 1,
     'two': 2,
     'three': 3,
     'four': 4,
     'five': 5,
     'six': 6,
     'seven': 7,
     'eight': 8,
     'nine': 9
 }

 calsum=0
 for calib in calibs:
     spelled_digits=(re.findall(r'(?:                                        one|two|three|four|five|six|seven|eight|nine)',calib))
     for dig in spelled_digits:
         calib=calib.replace(dig,str(digit_dict[dig]))
     print(calib)
     rcalib=calib[::-1]
     calsum+=int(re.search(r"\d",calib).group()+re.search(r"\d",rcalib).     group())
 print(calsum)
