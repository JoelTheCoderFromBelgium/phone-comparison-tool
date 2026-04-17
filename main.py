import requests
import smtplib

URL = "https://serpapi.com/search"
api_key = "YOUR_API_KEY_HERE"
MY_EMAIL = "YOUR_EMAIL_HERE"
MY_PASSWORD = "YOUR_APP_PASSWORD_HERE"

logo = r"""
 /$$$$$$$  /$$                                                                                                                              
| $$__  $$| $$                                                                                                                              
| $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$         /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$/| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$       /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$____/ | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$  /$$$$$$$| $$  \__/| $$$$$$$$| $$  \__/
| $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/      | $$      | $$  | $$| $$ | $$ | $$| $$  | $$ /$$__  $$| $$      | $$_____/| $$      
| $$      | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$      |  $$$$$$$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$      
|__/      |__/  |__/ \______/ |__/  |__/ \_______/       \_______/ \______/ |__/ |__/ |__/| $$____/  \_______/|__/       \_______/|__/      
                                                                                          | $$                                              
                                                                                          | $$                                                                                                                                        |__/                                              
"""

vs = r"""
 .----------------.  .----------------. 
| .--------------. || .--------------. |
| | ____   ____  | || |    _______   | |
| ||_  _| |_  _| | || |   /  ___  |  | |
| |  \ \   / /   | || |  |  (__ \_|  | |
| |   \ \ / /    | || |   '.___`-.   | |
| |    \ ' /     | || |  |`\____) |  | |
| |     \_/      | || |  |_______.'  | |
| |              | || |              | |
| '--------------' || '--------------' |
 '----------------'  '----------------' 
"""

print(logo)

first_phone = input("First phone: ")
print(vs)
second_phone = input("Second phone: ")

formatted_q = f"{first_phone} vs {second_phone} (I want 1 final phone and a link to purchase phone at its cheapest but I want trustable website)"

parameters = {
    "engine": "google_ai_mode",
    "q": formatted_q,
    "api_key": api_key,
}

response = requests.get(url=URL, params=parameters)
data = response.json()

formatted_a = f"Subject: {data['text_blocks'][0]['snippet_links'][0]['text']} vs {data['text_blocks'][0]['snippet_links'][1]['text']}\n\n{data['text_blocks'][0]['snippet']}"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="george.utib@gmail.com",
        msg=formatted_a
    )
