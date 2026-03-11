import json
import requests

# بيانات السيرفر
url = "http://vlcdc.org:80/player_api.php?username=lYG1EKR6m8&password=uXcRu8sQ2S&action=get_live_streams&category_id=1"

try:
    response = requests.get(url)
    data = response.json()

    def get_priority(name):
        n = name.lower()
        if 'arabic' in n or 'عربية' in n: return 1
        if 'french' in n or 'فرنسا' in n or 'fr' in n: return 2
        return 3

    # الترتيب
    sorted_data = sorted(data, key=lambda x: get_priority(x['name']))

    # حفظ النتائج
    with open('channels.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=4)
        
    print("Success: Channels sorted and saved to channels.json")

except Exception as e:
    print(f"Error: {e}")
