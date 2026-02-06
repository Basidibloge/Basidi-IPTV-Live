import requests

def update_ultra_global_organized():
    url = "http://4kgood.org/get.php?username=9680723188&password=kyft6ks0g7gr7uw0xio6&type=m3u"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            lines = response.text.splitlines()
            
            # مخازن التصنيف الشاملة
            cats = {
                "SPORTS": [], "ARABIC": [], "SERIES": [], "MOVIES": [],
                "FRENCH": [], "ENGLISH": [], "TURKISH": [], "GERMAN": [],
                "SPANISH": [], "KIDS": [], "DOCUMENTARY": []
            }
            
            current_info = ""
            for line in lines:
                if line.startswith("#EXTINF"):
                    current_info = line
                elif line.startswith("http"):
                    entry = f"{current_info}\n{line}\n"
                    info = current_info.upper()
                    
                    # الفرز الذكي
                    if any(x in info for x in ["SPORT", "BEIN", "SSC", "KASS"]): cats["SPORTS"].append(entry)
                    elif any(x in info for x in ["SERIES", "RAMADAN", "SHAHID", "مسلسلات"]): cats["SERIES"].append(entry)
                    elif any(x in info for x in ["MOVIE", "NETFLIX", "BOX", "سينما"]): cats["MOVIES"].append(entry)
                    elif any(x in info for x in ["FRANCE", "FR:", "CANAL"]): cats["FRENCH"].append(entry)
                    elif any(x in info for x in ["UK:", "USA:", "EN:", "ENGLISH"]): cats["ENGLISH"].append(entry)
                    elif any(x in info for x in ["TURK", "TR:"]): cats["TURKISH"].append(entry)
                    elif any(x in info for x in ["DE:", "GERMAN"]): cats["GERMAN"].append(entry)
                    elif any(x in info for x in ["ES:", "SPANISH"]): cats["SPANISH"].append(entry)
                    elif any(x in info for x in ["KIDS", "DISNEY", "CARTOON"]): cats["KIDS"].append(entry)
                    elif any(x in info for x in ["DOC", "NAT GEO", "WILD"]): cats["DOCUMENTARY"].append(entry)
                    elif any(x in info for x in ["ARABIC", "MBC", "OSN", "NILE"]): cats["ARABIC"].append(entry)

            # تجميع الـ 10,000 سطر (توزيع حصص لكل فئة)
            final_m3u = "#EXTM3U\n"
            # كل وحدة من هذه تأخذ عدداً معيناً من القنوات (القناة = سطرين)
            final_m3u += "".join(cats["SPORTS"][:800])      # 1600 سطر
            final_m3u += "".join(cats["ARABIC"][:800])      # 1600 سطر
            final_m3u += "".join(cats["SERIES"][:700])      # 1400 سطر
            final_m3u += "".join(cats["MOVIES"][:600])      # 1200 سطر
            final_m3u += "".join(cats["FRENCH"][:400])      # 800 سطر
            final_m3u += "".join(cats["ENGLISH"][:400])     # 800 سطر
            final_m3u += "".join(cats["TURKISH"][:400])     # 800 سطر
            final_m3u += "".join(cats["KIDS"][:400])        # 800 سطر
            final_m3u += "".join(cats["DOCUMENTARY"][:500]) # 1000 سطر
            
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(final_m3u)
                
            print("🚀 مبروك! السيرفر العالمي المنظم جاهز بـ 10,000 سطر.")
            
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    update_ultra_global_organized()
