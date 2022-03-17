from requests import get

print(get('http://127.0.0.1:8080/api/jobs').json())

print(get('http://127.0.0.1:8080/api/jobs/1').json())

print(get('http://127.0.0.1:8080/api/jobs/1000').json())

print(get('http://127.0.0.1:8080/api/jobs/qwe').json())
