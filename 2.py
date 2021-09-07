given_string = "python is my fav language"
index_num = 2

'''
result_string = ""
for i in range(len(given_string)):
    if i != index_num:
        result_string += given_string[i]'''

result_string = ''.join([given_string[i] for i in range(len(given_string)) if i != index_num])

print(result_string)
