import requests

def update_with_folders():
    url = "http://4kgood.org/get.php?username=9680723188&password=kyft6ks0g7gr7uw0xio6&type=m3u"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            lines = response.text.splitlines()
            
            # تعريف المجموعات
            groups = {
                "⚽ SPORTS": [], "🌍 ARABIC": [], "🎬 SERIES": [], "🎥 MOVIES": [],
                "🇫🇷 FRENCH": [], "🇬🇧 ENGLISH": [], "🇹🇷 TURKISH": [], "👶 KIDS": []
            }
            
            current_info = ""
            for line in lines:
                if line.startswith("#EXTINF"):
                    current_info = line
                elif line.startswith("http"):
                    info_up = current_info.upper()
                    # تحديد القسم وإضافة وسم المجلد group-title
                    tag = ""
                    if any(x in info_up for x in ["SPORT", "BEIN", "SSC"]): tag = "⚽ SPORTS"
                    elif any(x in info_up for x in ["SERIES", "RAMADAN", "SHAHID"]): tag = "🎬 SERIES"
                    elif any(x in info_up for x in ["MOVIE", "NETFLIX", "BOX"]): tag = "🎥 MOVIES"
                    elif any(x in info_up for x in ["FRANCE", "FR:"]): tag = "🇫🇷 FRENCH"
                    elif any(x in info_up for x in ["UK:", "USA:", "EN:"]): tag = "🇬🇧 ENGLISH"
                    elif any(x in info_up for x in ["TURK", "TR:"]): tag = "🇹🇷 TURKISH"
                    elif any(x in info_up for x in ["KIDS", "DISNEY", "CARTOON"]): tag = "👶 KIDS"
                    else: tag = "🌍 ARABIC"

                    # تعديل السطر لإضافة المجلد
                    new_info = current_info.replace('#EXTINF:-1,', f'#EXTINF:-1 group-title="{tag}",')
                    groups[tag].append(f"{new_info}\n{line}\n")

            # تجميع الـ 10,000 سطر
            final_m3u = "#EXTM3U\n"
            limit_per_cat = 600 # حوالي 1200 سطر لكل قسم
            for g_name in groups:
                final_m3u += "".join(groups[g_name][:limit_per_cat])
            
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(final_m3u)
            print("✅ تم إضافة وسوم المجموعات (group-title) بنجاح!")
            
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    update_with_folders()
