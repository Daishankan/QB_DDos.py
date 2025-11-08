# QB_DDos

أداة تعليمية لاختبار الإجهاد (DDoS) مكتوبة بلغة Python وتوجه الطلبات عبر Tor SOCKS5. **مخصصة للأغراض التعليمية فقط** — لا تستخدمها ضد أنظمة أو شبكات بدون إذن كتابي.

## المحتويات
- `QB_DDos.py` — ملف السكربت الرئيسي.

## المتطلبات
- Python 3.x
- مكتبة `pysocks`
- خدمة Tor تعمل على `127.0.0.1:9050` (مثال: تشغيل `tor` في Termux)

## التثبيت (Termux / Linux)
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install pysocks
# تثبيت tor إن لم يكن مثبتًا
pkg install tor -y
