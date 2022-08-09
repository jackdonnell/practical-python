contacts = {
    'number':4,
    'students':
    [
        {'name':'sarah', 'email':'sarah@gmail.com'},
        {'name': 'q', 'email':'q@gmail.com'},
        {'name': 'j', 'email':'j@gmail.com'},
        {'name': 'k', 'email':'k@gmail.com'}
    ]
}

for i in contacts['students']:
    print(i['email'])