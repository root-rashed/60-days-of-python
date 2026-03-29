with open('text.txt','r') as file:
    for line in file:
        print(line.strip())


new_text = 'so much'
with open('text.txt','a') as file:
    for line in new_text:
        file.write(line+'')
