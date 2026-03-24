search_word ='Analysis'
replace_word = 'Science'

with open(r'text.txt','+r') as file:
    data = file.read()
    data = data.replace(search_word,replace_word)


with open(r'text.txt','+w') as file:
    file.write(data)