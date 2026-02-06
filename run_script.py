import requests
import json

def get_channels():
    portal = "http://tv.saartv.cc/stalker_portal/server/load.php"
    mac = "00:1A:79:00:4D:84"
    
    # هيدرز أكثر دقة لمحاكاة جهاز MAG حقيقي
    headers = {
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (MAG210)',
        'X-User-Agent': 'Model: MAG210; Link: Ethernet',
        'Referer': 'http://tv.saartv.cc/stalker_portal/c/',
        'Accept': '*/*',
        'Cookie': f'mac={mac}; stb_lang=en; timezone=Africa/Casablanca',
        'Connection': 'Keep-Alive'
    }

    try:
        session = requests.Session()
        # 1. محاولة المصافحة (Handshake)
        handshake_url = f"{portal}?type=stb&action=handshake&JsHttpRequest=1-xml"
        token_res = session.get(handshake_url, headers=headers).json()
        
        token = token_res.get('js', {}).get('token')
        if not token:
            print("❌ لم يتم الحصول على التوكن، السيرفر قد يكون محظوراً أو الماك خاطئ")
            return

        headers['Authorization'] = f'Bearer {token}'

        # 2. جلب القنوات
        ch_url = f"{portal}?type=itv&action=get_all_channels&JsHttpRequest=1-xml"
        response = session.get(ch_url, headers=headers).json()
        channels = response.get('js', {}).get('data', [])

        if not channels:
            print("⚠️ السيرفر استجاب لكن قائمة القنوات فارغة")
            return

        m3u = "#EXTM3U\n"
        for ch in channels:
            name = ch.get('name')
            url = ch.get('cmd', '').replace('ffrt ', '').replace('ffmpeg ', '')
            if url:
                m3u += f"#EXTINF:-1, {name}\n{url}\n"
        
        with open("channels.m3u", "w", encoding="utf-8") as f:
            f.write(m3u)
        print(f"✅ نجاح! تم استخراج {len(channels)} قناة")

    except Exception as e:
        print(f"❌ خطأ تقني: {e}")

if __name__ == "__main__":
    get_channels()
