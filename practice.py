#numbers = [1,2,3,4,5,6]
#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print (even_numbers)

numbers = [1,2,3,4,5,6]
square = lambda x : x ** 2 
num_square = list(map(square, numbers))
print(num_square)

temu = [9,8,7,6,5,4,3,2,1]
sqr = lambda x : x >= 8
num_cube = list(filter(sqr, temu))
print(num_cube)

nomber = [1,2,3,4,5,6]

def square(num):
    return num  ** 2

skrnum = list(map(square, nomber))
print(skrnum)

def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))

#def pin_extractor(poem):
    #secret_code = ''
    #lines = poem.split('\n')
    #for line_index, line in enumerate(lines):
     #   words = line.split()
       # if secret_code += str(len(words[line_index])):
            
         #    return secret_code 

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))

#
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))



developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)



developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)
    