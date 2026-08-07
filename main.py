import json
from hadith_api import get_hadith, BOOKS
from chat import send_hadith

STATE_FILE = "state.json"


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)


def main():

    state = load_state()

    while True:

        book = BOOKS[state["book_index"]]

        result = get_hadith(book, state["page"])

        if len(result["data"]) == 0:

            state["book_index"] += 1
            state["page"] = 1

            if state["book_index"] >= len(BOOKS):
                state["book_index"] = 0

            continue

        hadith = result["data"][0]

        state["page"] += 1

        save_state(state)

        if hadith["status"] not in ["Sahih", "Hasan"]:
            continue

        send_hadith(hadith)

        break


if __name__ == "__main__":
    main()
