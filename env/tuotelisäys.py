import requests
import json

while True:
    tuote={'tuote':'Juusto'}
    lisättävä=input("Lisää tuote > ")
    tuote['tuote']=lisättävä
    msg=json.dumps(tuote)
    requests.post('http://127.0.0.1:5000/lisaatuote', data=msg)
    