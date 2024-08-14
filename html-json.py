from bs4 import BeautifulSoup
import json

file_name = input("Enter the path of your html file\nIf it is in the same directory as this script just enter the name of the file.\n")
with open(file_name, 'r', encoding='UTF-8') as file:
    try:
        html_content = file.read()
    except:
        print("Could not read file contents.")
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data
cards = []
for card_div in soup.find_all('div', class_='card'):
    title_div = card_div.find('div', class_='card-title')
    subtext_div = card_div.find('div', class_='card-subtext')
    button = card_div.find('button', class_='explain-button')

    card_data = {
        'title': title_div.text.strip() if title_div else '',
        'subtext': subtext_div.text.strip() if subtext_div else '',
        'onclick': button['onclick'].strip() if button else ''
    }

    cards.append(card_data)

# Convert the list of cards to JSON format
json_data = json.dumps(cards, indent=2)
with open('datax.json', 'w', encoding='UTF-8') as json_file:
    json_file.write(json_data)

print("Saved to json.")
