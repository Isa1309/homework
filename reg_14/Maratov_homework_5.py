import re


file_path = 'MOCK_DATA.txt'
result_file_path = 'Full_name.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()
what_search = r"[A-Z][a-z]+\W[A-Z][a-z]+\W[A-Z][a-z]*"
results = re.findall(what_search, my_text_file)

# Daniella	O' Loughran
# Horace	Woods

for item in results:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(results))}')
#
# [[A-Z]\w]+s[[A-Z]\w' ]*\s[[A-Z]\w]+