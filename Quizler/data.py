import requests

r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')

data = r.json()
question_data = data['results']

# print(question_data)