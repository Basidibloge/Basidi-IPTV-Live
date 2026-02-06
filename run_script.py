import requests

def get_bein_sports_package():
    # روابط لمصادر متخصصة في الرياضة و beIN
    # هذه الروابط يتم تحديثها يومياً من مطورين عالميين
    sources = [
        "https://raw.githubusercontent.com/m-v-p/Arabic_IPTV/main/Bein_Sports.m3u",
        "https://raw.githubusercontent.com/Yousof-H/IPTV/main/Sport.m3u",
        "https://iptv-org.github.io/iptv/categories/sports.m3u"
    ]
    
    combined_m3u = "#EXTM3U\n"
    print("📡 جاري البحث عن روابط beIN Sports الشغالة...")

    for url in sources:
        try:
            # إضافة User-Agent لتجنب الحظر أثناء السحب
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    if not line.startswith("#EXTM3U") and line.strip():
                        combined_m3u += line + "\n"
                print(f"✅ تم سحب قنوات من: {url}")
        except:
            print(f"❌ تعذر الاتصال بالمصدر: {url}")

    # حفظ الملف النهائي
    with open("channels.m3u", "w", encoding="utf-8") as f:
        f.write(combined_m3u)
    
    print("🚀 مبروك! ملف Basidi الآن يحتوي على باقة beIN كاملة.")

if __name__ == "__main__":
    get_bein_sports_package()
