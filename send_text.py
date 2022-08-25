from dotenv import load_dotenv
load_dotenv()

import os
key = os.environ.get("API_KEY")

print(key)