import requests

def test_connection():
    # رابط تجريبي لقنوات عربية عامة (لا يحتاج حماية)
    test_url = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"
    
    print("🔄 جاري فحص ترابط الملفات عبر الرابط التجريبي...")
    
    try:
        response = requests.get(test_url, timeout=15)
        if response.status_code == 200:
            content = response.text
            # حفظ المحتوى في ملف channels.m3u
            with open("channels.m3u", "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ تم جلب القنوات بنجاح! الملفات مترابطة 100%")
        else:
            print(f"❌ فشل الاتصال، كود الخطأ: {response.status_code}")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء جلب البيانات: {e}")

if __name__ == "__main__":
    test_connection()
