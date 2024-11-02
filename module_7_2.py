import io
from pprint import pprint


def custom_write(file_name, string):
    string_position = dict()
    i = 0
    while i < len(string):
        file = open(file_name, 'a', encoding='utf-8')
        bite_start = file.tell()
        file.write(string[i] + '\n')
        string_position.update({(i+1, bite_start):string[i]})
        file.close()
        i +=1
    return string_position


info = ['Text for tell', 'Используйте кодировку utf-8',
        'Because ther are 2 laguages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)