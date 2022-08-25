import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('API_KEY')
phone = os.environ.get('PHONE')
message = 'Hello world!!'

response = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': message,
    'key': key
})

print(response.json())