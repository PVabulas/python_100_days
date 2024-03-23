import requests

CATEGORIES = {
    "Any category": None,
    "General Knowledge": 9,
    "Books": 10,
    "Film": 11,
    "Music": 12,
    "Musicals and Theatres": 13,
    "Television": 14,
    "Video Games": 15,
    "Board Games": 16,
    "Science and Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
    "Comics": 29,
    "Gadgets": 30,
    "Japanese Anime & Manga": 31,
    "Cartoons & Animation": 32,
}
DIFFICULTIES = [None, "Easy", "Medium", "Hard"]
TYPES = [None, "multiple", "boolean"]


def get_questions():
    quiz_settings = {"amount": 10, "type": "boolean"}
    quiz_url = "https://opentdb.com/api.php"

    response = requests.get(quiz_url, params=quiz_settings)
    response.raise_for_status()
    return response.json()["results"]
