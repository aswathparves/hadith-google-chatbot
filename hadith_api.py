import os
import requests

API_KEY = os.environ["HADITH_API_KEY"]

BOOKS = [
    "sahih-bukhari",
    "sahih-muslim",
    "al-tirmidhi",
    "abu-dawood",
    "ibn-e-majah",
    "sunan-nasai"
]

BASE_URL = "https://www.hadithapi.com/public/api/hadiths"


def get_hadith(book, page):
    params = {
        "apiKey": API_KEY,
        "book": book,
        "paginate": 1,
        "page": page
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if data["status"] != 200:
        raise Exception(data["message"])

    return data["hadiths"]
