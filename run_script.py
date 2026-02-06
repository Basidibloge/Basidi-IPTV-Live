import requests

def update_from_4kgood():
    # رابط السيرفر الخاص بك
    url = "http://4kgood.org/get.php?username=9680723188&password=kyft6ks0g7gr7uw0xio6&type=m3u"
    
    print("📡 جاري جلب القنوات من سيرفر 4K Good...")
    
    try:
        # إضافة User-Agent لضمان قبول الطلب من السيرفر
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200 and "#EXTM3U" in response.text:
            # كتابة محتوى السيرفر بالكامل في ملفك
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"✅ مبروك! تم تحديث القنوات بنجاح من سيرفرك الخاص.")
        else:
            print(f"❌ فشل الجلب: السيرفر رد بكود {response.status_code} أو الرابط غير صحيح.")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    update_from_4kgood()
