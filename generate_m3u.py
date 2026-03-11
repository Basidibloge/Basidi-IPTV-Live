import json

# فتح ملف القنوات المرتب
with open('channels.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# إنشاء ملف M3U
with open('channels.m3u', 'w', encoding='utf-8') as f:
    f.write("#EXTM3U\n")
    for c in data:
        # رابط سيرفرك
        url = f"http://vlcdc.org:80/live/lYG1EKR6m8/uXcRu8sQ2S/{c['stream_id']}.m3u8"
        f.write(f'#EXTINF:-1,{c["name"]}\n{url}\n')
