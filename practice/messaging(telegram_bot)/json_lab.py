import json

# # dictionary 를 .json format으로 저장
# suji_data = {
#     'city': "Seoul",
#     'name': 'Suji',
#     'age': 22
# }
#
# with open('sujidata.json', 'w')as f:
#     json.dump(suji_data, f)

with open('sujidata.json', 'r')as f:
    data = json.load(f)

print(data)