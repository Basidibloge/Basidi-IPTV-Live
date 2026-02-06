import requests

def get_channels():
    portal = "http://tv.saartv.cc/stalker_portal/server/load.php"
    mac = "00:1A:79:00:4D:84"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (MAG210)',
        'X-User-Agent': 'Model: MAG210; Link: Ethernet',
        'Cookie': f'mac={mac}; stb_lang=en; timezone=Africa/Casablanca'
    }

    try:
        # 1. Handshake
        res = requests.get(f"{portal}?type=stb&action=handshake&JsHttpRequest=1-xml", headers=headers).json()
        token = res['js']['token']
        headers['Authorization'] = f'Bearer {token}'

        # 2. Get Channels
        data = requests.get(f"{portal}?type=itv&action=get_all_channels&JsHttpRequest=1-xml", headers=headers).json()
        channels = data.get('js', {}).get('data', [])

        # 3. Build M3U
        m3u = "#EXTM3U\n"
        for ch in channels:
            name = ch.get('name')
            url = ch.get('cmd', '').replace('ffrt ', '').replace('ffmpeg ', '')
            if url:
                m3u += f"#EXTINF:-1, {name}\n{url}\n"
        
        with open("channels.m3u", "w", encoding="utf-8") as f:
            f.write(m3u)
        print(f"✅ Successfully extracted {len(channels)} channels")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    get_channels()
