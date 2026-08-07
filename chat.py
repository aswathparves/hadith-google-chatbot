import os
import requests

WEBHOOK_URL = os.environ["GOOGLE_CHAT_WEBHOOK"]


def send_hadith(hadith):
    message = f"""📖 Hadith of the Day

📚 Book      : {hadith['book']['bookName']}
📖 Chapter   : {hadith['chapter']['chapterEnglish']}
🔢 Hadith No : {hadith['hadithNumber']}
👤 Narrator  : {hadith['englishNarrator']}
⭐ Grade      : {hadith['status']}

────────────────────────

{hadith['hadithEnglish']}
"""

    response = requests.post(
        WEBHOOK_URL,
        json={"text": message},
        timeout=30
    )

    response.raise_for_status()
