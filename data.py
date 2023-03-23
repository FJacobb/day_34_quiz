import requests
peremeter = {
    'amount':10,
    "type":"boolean",
    "category":18
}
data = requests.get(url="https://opentdb.com/api.php", params=peremeter)
data.raise_for_status()
data = data.json()
question_data =data["results"]

