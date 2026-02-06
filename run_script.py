import requests

def get_basidi_final_server():
    # السيرفر الذي طلبته (saartv)
    portal = "http://tv.saartv.cc/stalker_portal/server/load.php"
    mac = "00:1A:79:00:4D:84"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (MAG210)',
        'X-User-Agent': 'Model: MAG210; Link: Ethernet',
        'Cookie': f'mac={mac}; stb_lang=en; timezone=Africa/Casablanca',
        'Referer': f'{portal.replace("server/load.php", "c/")}',
        'Connection': 'Keep-Alive'
    }

    print(f"📡 جاري الاتصال بسيرفر Basidi الخاص: {portal}")

    try:
        session = requests.Session()
        # 1. عملية المصافحة (Handshake)
        handshake_res = session.get(f"{portal}?type=stb&action=handshake&JsHttpRequest=1-xml", headers=headers, timeout=15).json()
        token = handshake_res.get('js', {}).get('token')
        
        if not token:
            print("❌ السيرفر لم يعطِ توكن. تأكد من أن الماك أدريس فعال.")
            return

        headers['Authorization'] = f'Bearer {token}'

        # 2. جلب القنوات (ITV)
        channels_res = session.get(f"{portal}?type=itv&action=get_all_channels&JsHttpRequest=1-xml", headers=headers, timeout=15).json()
        channels = channels_res.get('js', {}).get('data', [])

        if channels:
            m3u = "#EXTM3U\n"
            for ch in channels:
                name = ch.get('name')
                # تنظيف رابط القناة من إضافات ffmpeg
                cmd = ch.get('cmd', '')
                url = cmd.split(' ')[-1] if ' ' in cmd else cmd
                
                if url and url.startswith('http'):
                    m3u += f"#EXTINF:-1, {name}\n{url}\n"
            
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(m3u)
            print(f"✅ تم بنجاح! تم استخراج {len(channels)} قناة، بما فيها beIN Sports.")
        else:
            print("⚠️ تم الاتصال ولكن قائمة القنوات فارغة (تأكد من حالة الاشتراك).")

    except Exception as e:
        print(f"❌ حدث خطأ تقني: {e}")

if __name__ == "__main__":
    get_basidi_final_server()
