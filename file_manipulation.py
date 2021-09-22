import json

# # Basic read in `simple.txt`
# myfile = open('data/simple.txt', 'r')
# my_paragraphs = myfile.read().splitlines()
# myfile.close()
#
# fixed_paragraphs = [i for i in my_paragraphs if i != '']
# print(fixed_paragraphs)
#
# # Using context manager
# with open("data/simple.txt", "r") as myfile:
#     my_paragraphs = myfile.read().splitlines()
#
# fixed_paragraphs = [i for i in my_paragraphs if i != '']
# print(fixed_paragraphs)


# Read in info from JSON file. Print out my user name is .... and my token is ....
with open('data/simple.json', 'r') as f:
    json_contents = json.load(f)
bizniz_pw = json_contents['bizniz']['my_token']
bizniz_user = json_contents['bizniz']['my_user']
print(f'My user name is {bizniz_user}.\nMy token is {bizniz_pw}')
