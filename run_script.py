import requests

def update_and_organize_final():
    url = "http://4kgood.org/get.php?username=9680723188&password=kyft6ks0g7gr7uw0xio6&type=m3u"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            lines = response.text.splitlines()
            
            # تصنيفات واضحة جداً
            categories = {
                "⚽ SPORTS": [],
                "🌍 ARABIC": [],
                "🎬 SERIES": [],
                "🎥 MOVIES": [],
                "👶 KIDS": [],
                "🇫🇷 FRENCH": [],
                "🇬🇧 ENGLISH": [],
                "🇹🇷 TURKISH": [],
                "📺 OTHERS": []
            }
            
            current_info = ""
            for line in lines:
                if line.startswith("#EXTINF"):
                    current_info = line
                elif line.startswith("http"):
                    # تنظيف اسم القناة لاستخراجه بدقة
                    raw_name = current_info.split(',')[-1].strip()
                    info_up = raw_name.upper()
                    
                    # اختيار القسم المناسب
                    if any(x in info_up for x in ["BEIN", "SPORT", "SSC", "KASS"]): tag = "⚽ SPORTS"
                    elif any(x in info_up for x in ["SERIES", "RAMADAN", "SHAHID", "مسلسلات"]): tag = "🎬 SERIES"
                    elif any(x in info_up for x in ["MOVIE", "NETFLIX", "BOX", "CINEMA"]): tag = "🎥 MOVIES"
                    elif any(x in info_up for x in ["FRANCE", "FR:", "CANAL"]): tag = "🇫🇷 FRENCH"
                    elif any(x in info_up for x in ["UK:", "USA:", "EN:", "ENGLISH"]): tag = "🇬🇧 ENGLISH"
                    elif any(x in info_up for x in ["TURK", "TR:"]): tag = "🇹🇷 TURKISH"
                    elif any(x in info_up for x in ["KIDS", "DISNEY", "CARTOON", "CN"]): tag = "👶 KIDS"
                    elif any(x in info_up for x in ["MBC", "OSN", "ROTANA", "NILE", "MOROCCO"]): tag = "🌍 ARABIC"
                    else: tag = "📺 OTHERS"

                    # بناء السطر الجديد بالتنسيق الذي تعشقه التطبيقات
                    formatted_entry = f'#EXTINF:-1 group-title="{tag}",{raw_name}\n{line}\n'
                    categories[tag].append(formatted_entry)

            # تجميع الـ 10,000 سطر (5000 قناة)
            final_content = "#EXTM3U\n"
            for group in categories:
                # نأخذ كمية متوازنة لضمان وجود كل الأقسام
                final_content += "".join(categories[group][:650])
            
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(final_content)
            print("✅ مبروك! الملف الآن مقسم ومجلد بالكامل وجاهز للاستخدام.")
            
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    update_and_organize_final()
