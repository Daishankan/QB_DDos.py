# QB_DDos

أداة تعليمية لاختبار الإجهاد (DDoS) مكتوبة بلغة Python وتوجه الطلبات عبر Tor SOCKS5.

> ⚠️ تحذير قانوني: هذه الأداة مخصصة لأغراض تعليمية فقط. لا تستخدمها ضد أي خادم أو شبكة بدون إذن خطي من مالك النظام.

---

## محتويات المستودع
- `QB_DDos.py` — سكربت الأداة الرئيسية.

---

## المتطلبات
- Python 3.x
- مكتبة `pysocks`
- خدمة Tor تعمل على `127.0.0.1:9050` (مثال: تشغيل `tor` في Termux)

---

## التثبيت (Termux / Linux)
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install pysocks
# لتثبيت tor (إن لم يكن مثبتًا)
pkg install tor -y

الإستخدام
python3 QB_DDos.py --server <TARGET_IP> --port <PORT> --threads <THREADS>
# مثال:
python3 QB_DDos.py --server 192.168.1.100 --port 80 --threads 100
