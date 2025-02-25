import requests

r = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
data = r.json()
question_data = data['results']

# print(json.dumps(question_data, indent=4))    
# print(question_data)
# print(type(question_data))
# print(question_data[0])
