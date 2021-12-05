from ui import UI
from question import Question


def fetch_trivia_data():
    """Fetch trivia questions using API."""
    import requests

    params = {
        'amount': 25,
        'type': "boolean"
    }
    resp = requests.get('https://opentdb.com/api.php', params=params)
    return resp.json()['results']


if __name__ == '__main__':
    questions = [Question(data['question'], data['correct_answer']) for data in fetch_trivia_data()]
    UI()
    