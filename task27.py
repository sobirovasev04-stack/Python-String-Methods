file = input('Fayl kiriting: ')

if  file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt'):
    print('True')
else:
    print('False')
