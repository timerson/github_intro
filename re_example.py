import re
import pprint

message = 'My cell number is 616-822-5636, my work number is 616-254-8170 and my home number is 616-464-3664'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#pprint.pprint(phoneNumRegex.findall(message))
mo = phoneNumRegex.findall(message)
for phoneNumber in mo:
    print(phoneNumber)
