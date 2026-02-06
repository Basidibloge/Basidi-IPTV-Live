import requests

def update_limited_channels():
    url = "http://4kgood.org/get.php?username=9680723188&password=kyft6ks0g7gr7uw0xio6&type=m3u"
    
    print("📡 جاري جلب أفضل 5000 قناة من السيرفر...")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            all_lines = response.text.splitlines()
            
            # التأكد من أن الملف يبدأ بـ #EXTM3U
            final_lines = []
            if all_lines[0].startswith("#EXTM3U"):
                final_lines.append(all_lines[0])
            
            # أخذ أول 10,000 سطر بعد سطر البداية
            # هذا سيعطيك حوالي 5000 قناة (كل قناة اسم ورابط)
            limit = 10000
            count = 0
            for line in all_lines[1:]:
                if count < limit:
                    final_lines.append(line)
                    count += 1
                else:
                    break
            
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write("\n".join(final_lines))
                
            print(f"✅ تم! الملف الآن يحتوي على {len(final_lines)} سطر فقط.")
            
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    update_limited_channels()
