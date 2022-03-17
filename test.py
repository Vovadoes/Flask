from random import randint

from requests import get, post

# корректный ввод
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'Текст новости',
                 'work_size': 1,
                 'collaborators': [1],
                 'is_finished': False}).json())

# получаем все работы

js = get('http://localhost:8080/api/jobs').json()

number = randint(0, 65535)
while number in [i["id"] for i in js["jobs"]]:
    number = randint(0, 65535)
# корректный ввод
print(post('http://localhost:8080/api/jobs',
           json={'id': number,
                 'team_leader': 1,
                 'job': 'Текст новости',
                 'work_size': 1,
                 'collaborators': [1],
                 'is_finished': False}).json())

# неверный ввод
print(post('http://localhost:8080/api/jobs',
           json={'id': 1,
                 'team_leader': False,
                 'job': 'Текст новости',
                 'work_size': 1,
                 'collaborators': '',
                 'is_finished': 2131232}).json())

# нехватка данных
print(post('http://localhost:8080/api/jobs',
           json={}).json())
